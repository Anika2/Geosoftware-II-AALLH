# xml for the update transaction
# @author: Anika Graupner 

from lxml import etree

updatexml = """<?xml version="1.0" encoding="UTF-8"?>
<csw:Transaction xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" xmlns:ows="http://www.opengis.net/ows" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/cat/csw/2.0.2 http://schemas.opengis.net/csw/2.0.2/CSW-publication.xsd" service="CSW" version="2.0.2">
<csw:Update>
<gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gco="http://www.isotc211.org/2005/gco" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.isotc211.org/2005/gmd http://schemas.opengis.net/csw/2.0.2/profiles/apiso/1.0.0/apiso.xsd">
	<gmd:fileIdentifier>
		<gco:CharacterString>%(id)s</gco:CharacterString>
	</gmd:fileIdentifier>
	<gmd:hierarchyLevel>
		<gmd:MD_ScopeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_ScopeCode" codeListValue="dataset"/>
	</gmd:hierarchyLevel>
	<gmd:contact>
		<gmd:CI_ResponsibleParty>
			<gmd:organisationName>
				<gco:CharacterString>pycsw</gco:CharacterString>
			</gmd:organisationName>
			<gmd:role>
				<gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode" codeListValue="publisher"/>
			</gmd:role>
		</gmd:CI_ResponsibleParty>
	</gmd:contact>
	<gmd:dateStamp>
		<gco:Date>2011-05-17</gco:Date>
	</gmd:dateStamp>
	<gmd:identificationInfo>
		<gmd:MD_DataIdentification>
			<gmd:citation>
				<gmd:CI_Citation>
					<gmd:title>
						<gco:CharacterString>pycsw record</gco:CharacterString>
					</gmd:title>
					<gmd:date>
						<gmd:CI_Date>
							<gmd:date>
								<gco:Date>2011-05-17</gco:Date>
							</gmd:date>
							<gmd:dateType>
								<gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode" codeListValue="revision"/>
							</gmd:dateType>
						</gmd:CI_Date>
					</gmd:date>
				</gmd:CI_Citation>
			</gmd:citation>
			<gmd:abstract>
				<gco:CharacterString>Sample metadata record updated</gco:CharacterString>
			</gmd:abstract>
			<gmd:language>
				<gco:CharacterString>eng</gco:CharacterString>
			</gmd:language>
			<gmd:extent>
				<gmd:EX_Extent>
					<gmd:geographicElement>
						<gmd:EX_GeographicBoundingBox>
							<gmd:westBoundLongitude>
								<gco:Decimal>-180</gco:Decimal>
							</gmd:westBoundLongitude>
							<gmd:eastBoundLongitude>
								<gco:Decimal>180</gco:Decimal>
							</gmd:eastBoundLongitude>
							<gmd:southBoundLatitude>
								<gco:Decimal>-90</gco:Decimal>
							</gmd:southBoundLatitude>
							<gmd:northBoundLatitude>
								<gco:Decimal>90</gco:Decimal>
							</gmd:northBoundLatitude>
						</gmd:EX_GeographicBoundingBox>
					</gmd:geographicElement>
                    <gmd:temporalElement>
						<gmd:EX_TemporalExtent>
							<gmd:extent>
								<gml:TimePeriod gml:id="IDcd3b1c4f-b5f7-439a-afc4-3317a4cd89be" xsi:type="gml:TimePeriodType">
									<gml:beginPosition>2011-04-18</gml:beginPosition>
									<gml:endPosition>2011-04-20</gml:endPosition>
								</gml:TimePeriod>
							</gmd:extent>
						</gmd:EX_TemporalExtent>
				</gmd:temporalElement>
				</gmd:EX_Extent>
			</gmd:extent>
		</gmd:MD_DataIdentification>
	</gmd:identificationInfo>
</gmd:MD_Metadata>
</csw:Update>
</csw:Transaction>"""

print(updatexml)






