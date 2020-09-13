# importing etree from lxml module 
from lxml import etree 

root_elem = etree.Element('html') 
etree.SubElement(root_elem, 'head') 
etree.SubElement(root_elem, 'title') 
etree.SubElement(root_elem, 'body') 

print(etree.tostring(root_elem, pretty_print = True).decode("utf-8"))