import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class DrawioBuilder:
    # Style constants
    ST_START = "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;"
    ST_END = "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontStyle=1;fontSize=12;"
    ST_PROC = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;"
    ST_PROC_RECT = "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;"
    ST_INPUT = "shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;"
    ST_OUTPUT = "shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;"
    ST_DEC = "strokeWidth=2;html=1;shape=mxgraph.flowchart.decision;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#000000;fontColor=#000000;fontSize=12;"
    ST_SWIM = "swimlane;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;strokeWidth=2;fontStyle=1;fontSize=14;fontColor=#000000;align=center;"
    ST_CYL = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;size=10;"
    ST_DOC = "shape=document;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;size=0.2;"
    ST_TRAP = "verticalLabelPosition=middle;verticalAlign=middle;html=1;shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;size=0.23;arcSize=10;flipV=1;labelPosition=center;align=center;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=12;"

    EDGE_BASE = ("edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;"
                 "jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.5;"
                 "fontColor=#000000;fontSize=11;labelBackgroundColor=#FFFFFF;")

    def __init__(self, name, page_id, page_w=850, page_h=1100):
        self.name = name
        self.page_id = page_id
        self.page_w = page_w
        self.page_h = page_h
        self.counter = 0
        self.nodes = []
        self.edges = []

    def _next_id(self, prefix):
        self.counter += 1
        return f"{prefix}{self.counter}"

    def add(self, nid, label, kind, x, y, w=None, h=None, parent="1"):
        if kind == "start":
            w = w or 120
            h = h or 50
            style = self.ST_START
        elif kind == "end":
            w = w or 120
            h = h or 50
            style = self.ST_END
        elif kind == "process":
            w = w or 160
            h = h or 55
            style = self.ST_PROC
        elif kind == "process_rect":
            w = w or 160
            h = h or 55
            style = self.ST_PROC_RECT
        elif kind == "input":
            w = w or 175
            h = h or 55
            style = self.ST_INPUT
        elif kind == "output":
            w = w or 175
            h = h or 55
            style = self.ST_OUTPUT
        elif kind == "decision":
            w = w or 110
            h = h or 80
            style = self.ST_DEC
        elif kind == "swimlane":
            w = w or 400
            h = h or 1000
            style = self.ST_SWIM
        elif kind == "cylinder":
            w = w or 140
            h = h or 60
            style = self.ST_CYL
        elif kind == "document":
            w = w or 190
            h = h or 70
            style = self.ST_DOC
        elif kind == "trapezoid":
            w = w or 180
            h = h or 60
            style = self.ST_TRAP
        else:
            w = w or 150
            h = h or 50
            style = self.ST_PROC
        self.nodes.append({
            "id": nid, "value": label, "style": style,
            "x": x, "y": y, "w": w, "h": h, "parent": parent
        })

    def link(self, src, dst, label="", exit_pt=None, entry_pt=None, points=None):
        eid = self._next_id("e")
        style = self.EDGE_BASE
        if exit_pt:
            style += f"exitX={exit_pt[0]};exitY={exit_pt[1]};exitDx=0;exitDy=0;"
        if entry_pt:
            style += f"entryX={entry_pt[0]};entryY={entry_pt[1]};entryDx=0;entryDy=0;"
        
        self.edges.append({
            "id": eid, "value": label, "style": style,
            "source": src, "target": dst, "points": points or [],
        })

    def save(self, filepath):
        mxfile = ET.Element("mxfile", host="Electron", version="21.6.8",
                            modified="2026-06-05T14:00:00.000Z",
                            agent="Mozilla/5.0", type="device")
        diagram = ET.SubElement(mxfile, "diagram", id=self.page_id, name=self.name)
        model = ET.SubElement(diagram, "mxGraphModel", 
                              dx="1000", dy="1000", grid="1", gridSize="10",
                              guides="1", tooltips="1", connect="1", arrows="1",
                              fold="1", page="1", pageScale="1",
                              pageWidth=str(self.page_w), pageHeight=str(self.page_h),
                              math="0", shadow="0")
        root = ET.SubElement(model, "root")
        
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")

        # Build Vertices
        for n in self.nodes:
            cell = ET.SubElement(root, "mxCell", id=n["id"], value=n["value"],
                                 style=n["style"], vertex="1", parent=n["parent"])
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

        # Add transparent Frame node for headless renderer cropping bounding box
        frame_cell = ET.SubElement(root, "mxCell", id="frame", value="",
                                   style="fillColor=none;strokeColor=none;connectable=0;allowArrows=0;",
                                   vertex="1", parent="1")
        geom_frame = ET.SubElement(frame_cell, "mxGeometry", x="0", y="0",
                                   width=str(self.page_w), height=str(self.page_h))
        geom_frame.set("as", "geometry")

        # Format XML (Pretty Print)
        raw = ET.tostring(mxfile, encoding="utf-8")
        dom = minidom.parseString(raw)
        pretty_xml = dom.toprettyxml(indent="  ")
        if pretty_xml.startswith("<?xml"):
            pretty_xml = pretty_xml.split("\n", 1)[1]
        out_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + pretty_xml

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(out_content)
        print(f"Generated Draw.io XML at: {filepath}")

def build_sistem_baru():
    b = DrawioBuilder("Sistem Baru", "page-baru", 880, 1050)
    # Add Swimlanes
    b.add("lane_petani", "PETANI", "swimlane", 40, 20, 400, 1000)
    b.add("lane_sistem", "SISTEM", "swimlane", 440, 20, 400, 1000)

    # Petani lane nodes
    b.add("mulai", "Mulai", "start", 140, 50, parent="lane_petani")
    b.add("amati", "Petani mengamati gejala pada\ntanaman kangkung", "trapezoid", 110, 150, parent="lane_petani")
    b.add("pilih", "Pilih gejala yang dialami", "input", 112.5, 270, parent="lane_petani")
    b.add("input_cf", "Input nilai keyakinan (CF user)\n0 ~ 1", "input", 112.5, 390, parent="lane_petani")
    b.add("tampil_hasil", "Tampilkan hasil diagnosa\n(penyakit, CF, persentase,\ndeskripsi, solusi)", "document", 105, 730, parent="lane_petani")
    b.add("selesai", "Selesai", "end", 140, 890, parent="lane_petani")

    # Sistem lane nodes
    b.add("db", "Database", "cylinder", 130, 150, parent="lane_sistem")
    b.add("proses_cf", "Proses Certainty Factor\n(CF)\nKombinasi CF user + CF\npakar", "process_rect", 120, 382.5, parent="lane_sistem")
    b.add("teridentifikasi", "Penyakit\nteridentifikasi?", "decision", 135, 560, parent="lane_sistem")

    # Links
    b.link("mulai", "amati")
    b.link("amati", "pilih")
    b.link("pilih", "input_cf")
    
    # Input CF -> Proses CF (across lanes)
    b.link("input_cf", "proses_cf", exit_pt=(1, 0.5), entry_pt=(0, 0.5))
    
    # DB -> Proses CF
    b.link("db", "proses_cf", exit_pt=(0.5, 1), entry_pt=(0.5, 0))
    
    # Proses CF -> DB loop
    b.link("proses_cf", "db", exit_pt=(1, 0.5), entry_pt=(1, 0.5),
           points=[(760, 437.5), (760, 200)])

    # Proses CF -> Teridentifikasi
    b.link("proses_cf", "teridentifikasi", exit_pt=(0.5, 1), entry_pt=(0.5, 0))

    # Teridentifikasi -> Tampil Hasil (Ya)
    b.link("teridentifikasi", "tampil_hasil", label="Ya", exit_pt=(0.5, 1), entry_pt=(0.5, 0),
           points=[(640, 700), (240, 700)])

    # Teridentifikasi -> Pilih (Tidak)
    b.link("teridentifikasi", "pilih", label="Tidak", exit_pt=(0, 0.5), entry_pt=(0, 0.5),
           points=[(100, 620), (100, 317.5)])

    # Tampil Hasil -> DB loop (Update history/stats)
    b.link("tampil_hasil", "db", exit_pt=(1, 0.5), entry_pt=(1, 0.5),
           points=[(810, 790), (810, 200)])

    # Tampil Hasil -> Selesai
    b.link("tampil_hasil", "selesai")

    b.save("/var/home/indra12/skripsi/kangkungku/diagram/flowchart/06-flowchart-sistem-baru.drawio")

def build_sistem_lama():
    b = DrawioBuilder("Sistem Lama", "page-lama", 880, 1250)
    # Add Swimlanes
    b.add("lane_petani", "Petani", "swimlane", 40, 20, 400, 1200)
    b.add("lane_pakar", "PAKAR", "swimlane", 440, 20, 400, 1200)

    # Petani lane nodes
    b.add("mulai", "Mulai", "start", 140, 25, parent="lane_petani")
    b.add("masalah", "Petani menemukan masalah pada\ntanaman kangkung", "trapezoid", 110, 95, parent="lane_petani")
    b.add("amati", "Mengamati gejala secara manual", "trapezoid", 110, 165, parent="lane_petani")
    b.add("catat", "Mencatat gejala yang diamati", "input", 112.5, 245, parent="lane_petani")
    b.add("identifikasi_sendiri", "Bisa identifikasi sendiri?", "decision", 135, 325, parent="lane_petani")
    
    b.add("pakar_cari_petani", "Mencari pakar pertanian /\npenyuluh lapangan", "trapezoid", 110, 455, parent="lane_petani")
    b.add("pakar_tersedia", "Pakar tersedia?", "decision", 135, 605, parent="lane_petani")
    b.add("pakar_tunggu", "Menunggu jadwal\nkunjungan pakar", "trapezoid", 110, 735, parent="lane_petani")
    b.add("pakar_ulangi", "Ulangi konsultasi ke\npakar", "trapezoid", 110, 815, parent="lane_petani")
    b.add("pakar_solusi_terap", "Petani menerapkan solusi\npenanganan", "trapezoid", 110, 895, parent="lane_petani")
    b.add("tanaman_sembuh", "Tanaman sembuh?", "decision", 135, 985, parent="lane_petani")
    b.add("selesai", "Selesai", "end", 140, 1115, parent="lane_petani")

    # Middle column absolute nodes (placed between Petani and Pakar)
    b.add("pakar_cari_mid", "Mencari pakar pertanian /\npenyuluh lapangan", "trapezoid", 350, 385, parent="1")
    b.add("pakar_catat_mid", "Mencatat hasil identifikasi", "input", 352.5, 455, parent="1")
    b.add("pakar_akurat_mid", "Hasil akurat?", "decision", 375, 525, parent="1")

    # Pakar lane nodes
    b.add("pakar_periksa", "Pakar memeriksa tanaman\nlangsung", "trapezoid", 110, 605, parent="lane_pakar")
    b.add("pakar_diagnosa", "Pakar memberikan diagnosis\npenyakit", "document", 105, 675, parent="lane_pakar")
    b.add("pakar_solusi", "Pakar memberikan solusi\npenanganan", "trapezoid", 110, 745, parent="lane_pakar")

    # Links
    b.link("mulai", "masalah")
    b.link("masalah", "amati")
    b.link("amati", "catat")
    b.link("catat", "identifikasi_sendiri")
    
    b.link("identifikasi_sendiri", "pakar_cari_mid", label="Ya", exit_pt=(1, 0.5), entry_pt=(0, 0.5))
    b.link("identifikasi_sendiri", "pakar_cari_petani", label="Tidak", exit_pt=(0.5, 1), entry_pt=(0.5, 0))

    b.link("pakar_cari_mid", "pakar_catat_mid")
    b.link("pakar_catat_mid", "pakar_akurat_mid")

    b.link("pakar_akurat_mid", "pakar_cari_petani", label="Tidak", exit_pt=(0, 0.5), entry_pt=(1, 0.5))
    b.link("pakar_akurat_mid", "pakar_solusi_terap", label="Ya", exit_pt=(0.5, 1), entry_pt=(0.5, 0),
           points=[(440, 880), (240, 880)])

    b.link("pakar_cari_petani", "pakar_tersedia")
    b.link("pakar_tersedia", "pakar_tunggu", label="Tidak", exit_pt=(0.5, 1), entry_pt=(0.5, 0))
    b.link("pakar_tunggu", "pakar_tersedia", exit_pt=(0, 0.5), entry_pt=(0, 0.5),
           points=[(90, 785), (90, 665)])

    b.link("pakar_tersedia", "pakar_periksa", label="Ya", exit_pt=(1, 0.5), entry_pt=(0, 0.5))

    b.link("pakar_periksa", "pakar_diagnosa")
    b.link("pakar_diagnosa", "pakar_solusi")

    b.link("pakar_solusi", "pakar_solusi_terap", exit_pt=(0, 0.5), entry_pt=(1, 0.5))

    b.link("pakar_solusi_terap", "tanaman_sembuh")
    b.link("tanaman_sembuh", "selesai", label="Ya", exit_pt=(0.5, 1), entry_pt=(0.5, 0))
    b.link("tanaman_sembuh", "pakar_ulangi", label="Tidak", exit_pt=(0, 0.5), entry_pt=(1, 0.5))

    b.link("pakar_ulangi", "pakar_cari_petani", exit_pt=(0, 0.5), entry_pt=(0, 0.5),
           points=[(90, 865), (90, 505)])

    b.save("/var/home/indra12/skripsi/kangkungku/diagram/flowchart/05-flowchart-sistem-lama.drawio")

if __name__ == "__main__":
    os.makedirs("/var/home/indra12/skripsi/kangkungku/diagram/flowchart", exist_ok=True)
    build_sistem_baru()
    build_sistem_lama()
