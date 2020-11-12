# Parsing XML to Python is tricky as XML is verbose and the tags don't always map neatly into Python
# Additionally it is not always clear how the attribute values should be represented in data.

# Cisco provides tools, example being YANG-CLI, which takes the XML output and identifies the relevant 
# XML data based on YANG modelling. This file will focus on such a YANG-based translation.

"""
<?xml version="1.0" encoding="UTF-8"?>

<rpc message-id="1"
 xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <edit-config>
  <target>
   <candidate/>
  </target>
  <default-operation>merge</default-operation>
  <test-option>set</test-option>
  <config>
   <int8.1
    xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
    nc:operation="create"
    xmlns="http://netconfcentral.org/ns/test">9</int8.1>
  </config>
 </edit-config>
</rpc>
"""

# Begin by importing the required libraries 
import xml.etree.ElementTree as ET          # ElementTree helper library
import re                                   # regular expression engine

# Use the PARSE function from ET (ElementTree) to parse the file, 'myfile.xml'
xml = ET.parse("myfile.xml")

# Access the root element of the xml file with the getroot() function
root = xml.getroot()

# With the file parsed and the root identified, regular expressions can be used to check for target expressions
ns = re.match(r'{.*}', root.tag).group(0)       # Isolates the document's namespace value
editconf = root.find(f"{ns}edit-config")        
defop = editconf.find(f"{ns}default-operation")
testopt = editconf.find(f"{ns}test-option")

# Print the value for the default operation and test option - the PARSER gathered this detail in the above snippet
print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testopt.text)


# Python's xml.etree.ElementTree module is used to PARSE the XML data
# In this instance, the code uses the 'fromstring' method which parses XML in a string and not a file

# It returns a tree data structure containing the parsed data
# the root of this data can be obtained by calling the structure's getroot() method
# The top level of the tree can be searched for the containing tag <edit-config> and when found
# the tagged block can be searched for two named values that it contains

