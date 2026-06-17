import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os

class ERDBuilder:
    def __init__(self, name, page_id, page_w=1100, page_h=850):
        self.name = name
        self.page_id = page_id
        self.page_w = page_w
        self.page_h = page_h
        self.counter = 0
        self.nodes = []
        self.edges = []
        self.titles = []

    def _next_id(self, prefix):
        self.counter += 1
        return f"{prefix}{self.counter}"

    def add_table(self, nid, name, attributes, x, y, w, h):
        # Format HTML table value
        attr_html = "".join([f"{a}<br/>" for a in attributes[:-1]] + [attributes[-1]]) if attributes else ""
        label = (
            f'<div style="text-align: center; font-weight: bold; border-bottom: 1px solid #000000; '
            f'padding-bottom: 4px; margin-bottom: 6px; font-size: 13px;">{name}</div>{attr_html}'
        )
        style = (
            "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;"
            "align=left;verticalAlign=top;spacingLeft=8;spacingRight=8;spacingTop=6;spacingBottom=6;"
            "fontColor=#000000;fontSize=12;fontFamily=Helvetica;"
        )
        self.nodes.append({
            "id": nid, "value": label, "style": style,
            "x": x, "y": y, "w": w, "h": h
        })

    def add_title(self, label, x=50, y=30, w=500, h=30):
        self.titles.append({
            "id": self._next_id("title"),
            "value": label,
            "x": x, "y": y, "w": w, "h": h,
        })

    def link_crow_foot(self, src, dst, label="", exit_pt=(0.5, 1), entry_pt=(0.5, 0), points=None):
        eid = self._next_id("e")
        style = (
            "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
            "strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=10;labelBackgroundColor=#FFFFFF;"
            "startArrow=ERone;endArrow=ERmany;startSize=10;endSize=10;"
            f"exitX={exit_pt[0]};exitY={exit_pt[1]};exitDx=0;exitDy=0;"
            f"entryX={entry_pt[0]};entryY={entry_pt[1]};entryDx=0;entryDy=0;"
        )
        self.edges.append({
            "id": eid, "value": label, "style": style,
            "source": src, "target": dst, "points": points or []
        })

    def save(self, filepath):
        mxfile = ET.Element("mxfile", host="Electron", version="21.6.8",
                            modified="2026-06-17T12:00:00.000Z",
                            agent="Mozilla/5.0", type="device")
        diagram = ET.SubElement(mxfile, "diagram", id=self.page_id, name=self.name)
        model = ET.SubElement(diagram, "mxGraphModel",
                               dx="1000", dy="1000", grid="1", gridSize="10",
                               guides="1", tooltips="1", connect="1", arrows="1",
                               fold="1", page="1", pageScale="1",
                               pageWidth=str(self.page_w), pageHeight=str(self.page_h),
                               math="0", shadow="0")
        root = ET.SubElement(model, "root")

        # Mandatory layer cells
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")

        # Build Titles
        for t in self.titles:
            cell = ET.SubElement(root, "mxCell", id=t["id"], value=t["value"],
                                 style=("text;html=1;align=left;verticalAlign=middle;"
                                        "whiteSpace=wrap;rounded=0;fontSize=16;"
                                        "fontStyle=1;fontColor=#000000;"),
                                 vertex="1", parent="1")
            geom = ET.SubElement(cell, "mxGeometry",
                                 x=str(t["x"]), y=str(t["y"]),
                                 width=str(t["w"]), height=str(t["h"]))
            geom.set("as", "geometry")

        # Build Tables
        for n in self.nodes:
            cell = ET.SubElement(root, "mxCell", id=n["id"], value=n["value"],
                                 style=n["style"], vertex="1", parent="1")
            geom = ET.SubElement(cell, "mxGeometry",
                                 x=str(n["x"]), y=str(n["y"]),
                                 width=str(n["w"]), height=str(n["h"]))
            geom.set("as", "geometry")

        # Build Edges
        for e in self.edges:
            cell = ET.SubElement(root, "mxCell", id=e["id"], value=e["value"],
                                 style=e["style"], edge="1", parent="1",
                                 source=e["source"], target=e["target"])
            geom = ET.SubElement(cell, "mxGeometry", relative="1")
            geom.set("as", "geometry")
            if e["points"]:
                arr = ET.SubElement(geom, "Array")
                arr.set("as", "points")
                for (px, py) in e["points"]:
                    ET.SubElement(arr, "mxPoint", x=str(px), y=str(py))

        raw = ET.tostring(mxfile, encoding="utf-8")
        dom = minidom.parseString(raw)
        pretty_xml = dom.toprettyxml(indent="  ")
        if pretty_xml.startswith("<?xml"):
            pretty_xml = pretty_xml.split("\n", 1)[1]
        out_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + pretty_xml

        # Ensure directory exists
        dirname = os.path.dirname(filepath)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(out_content)
        print(f"Successfully generated {filepath}")

if __name__ == "__main__":
    builder = ERDBuilder("Entity Relationship Diagram (ERD)", "erd-page-1")
    builder.add_title("Entity Relationship Diagram (ERD) - KangkungKu")

    # Table: users
    builder.add_table(
        "t_users", "users",
        [
            "<b><u>id</u></b> : INTEGER",
            "username : VARCHAR(35)",
            "hashed_password : VARCHAR(64)",
            "role : VARCHAR(20)",
            "is_active : BOOLEAN",
            "alamat : TEXT"
        ],
        x=50, y=100, w=240, h=160
    )

    # Table: diagnosa_history
    builder.add_table(
        "t_diagnosa_history", "diagnosa_history",
        [
            "<b><u>id</u></b> : INTEGER",
            "<i>user_id</i> : INTEGER",
            "<i>penyakit_id</i> : INTEGER",
            "faktor_kepastian : FLOAT",
            "persentase : FLOAT",
            "gejala_input : TEXT",
            "created_at : VARCHAR(50)"
        ],
        x=400, y=90, w=250, h=180
    )

    # Table: penyakit
    builder.add_table(
        "t_penyakit", "penyakit",
        [
            "<b><u>id</u></b> : INTEGER",
            "nama : VARCHAR(35)",
            "deskripsi : TEXT",
            "solusi : TEXT",
            "url_gambar : VARCHAR(255)"
        ],
        x=760, y=250, w=240, h=140
    )

    # Table: gejala
    builder.add_table(
        "t_gejala", "gejala",
        [
            "<b><u>id</u></b> : INTEGER",
            "kode : VARCHAR(35)",
            "deskripsi : VARCHAR(35)",
            "url_gambar : VARCHAR(255)"
        ],
        x=50, y=420, w=240, h=120
    )

    # Table: aturan
    builder.add_table(
        "t_aturan", "aturan",
        [
            "<b><u>id</u></b> : INTEGER",
            "<i>penyakit_id</i> : INTEGER",
            "<i>gejala_id</i> : INTEGER",
            "pakar_cf : FLOAT"
        ],
        x=400, y=420, w=240, h=120
    )

    # Links / Relationships:
    # 1. users (1) to diagnosa_history (many)
    builder.link_crow_foot(
        "t_users", "t_diagnosa_history",
        label="memiliki",
        exit_pt=(1, 0.5), entry_pt=(0, 0.5)
    )

    # 2. gejala (1) to aturan (many)
    builder.link_crow_foot(
        "t_gejala", "t_aturan",
        label="memiliki",
        exit_pt=(1, 0.5), entry_pt=(0, 0.5)
    )

    # 3. penyakit (1) to diagnosa_history (many)
    # exit left of penyakit, enter right of diagnosa_history. Route via x=700
    builder.link_crow_foot(
        "t_penyakit", "t_diagnosa_history",
        label="tercatat_di",
        exit_pt=(0, 0.3), entry_pt=(1, 0.7),
        points=[(700, 292), (700, 216)]
    )

    # 4. penyakit (1) to aturan (many)
    # exit left of penyakit, enter right of aturan. Route via x=700
    builder.link_crow_foot(
        "t_penyakit", "t_aturan",
        label="memiliki",
        exit_pt=(0, 0.7), entry_pt=(1, 0.5),
        points=[(700, 348), (700, 480)]
    )

    # Save to both target locations
    builder.save("erd.drawio")
    builder.save("diagram/erd.drawio")
