# -*- coding: utf-8 -*-
import pydot,sys
import xml.etree.ElementTree as ET
 
def main(f):
    tree = ET.parse(f)
    elem = tree.getroot()
    for dependencies in elem.findall(".//dependencies"):
        edge = []
        if dependencies.attrib.get("type") == "collapsed-dependencies":                
            for dep in dependencies.findall(".//dep"):
                dep_tuple = (dep[0].text,dep[1].text)
                if "," in dep_tuple or "." in dep_tuple:
                    pass
                else:
                    edge.append(dep_tuple)
        if len(edge) != 0:           
            g = pydot.graph_from_edges(edge, directed = True)
            g.write_jpeg("test_graph.jpg", prog='dot')
            #初めの分だけグラフを作りたかったので 
            break
if __name__ == "__main__":
    main(sys.stdin)
