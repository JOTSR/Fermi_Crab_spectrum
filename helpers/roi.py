import xml.etree.ElementTree as ET

def set_free_xml(xml_path: str, ref_name: str, ceil: float, xml_out_path: str = None):
    xml = ET.parse(xml_path)
    root = xml.getroot()

    def get_pos(name: str):
        for source in root.findall("source"):
            s_name = source.get("name")
            if type(s_name) != str:
                continue
            if name in s_name:
                ra = source.find("spatialModel").find("parameter[@name='RA']").get("value")
                dec = source.find("spatialModel").find("parameter[@name='DEC']").get("value")
                return (float(ra), float(dec))

    [ref_ra, ref_dec] = get_pos(ref_name)

    def lock_spectrum(source: ET.Element, locked: bool):
        free = "0" if locked else "1"
        for params in source.findall("spectrum/parameter"):
            params.set("free", free)


    for source in root.findall("source"):
        ra = source.find("spatialModel").find("parameter[@name='RA']")
        dec = source.find("spatialModel").find("parameter[@name='DEC']")
        if ra == None or dec == None:
            continue
        if (ref_ra + ceil) < float(ra.get("value")) < (ref_ra - ceil):
            lock_spectrum(source, True)
            continue
        if (ref_dec + ceil) < float(dec.get("value")) < (ref_dec - ceil):
            lock_spectrum(source, True)
            continue
        lock_spectrum(source, False)

    xml.write(xml_path if xml_out_path == None else xml_out_path)