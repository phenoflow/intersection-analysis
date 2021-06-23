import json, re
with open("siblings.json") as siblings:
  siblings = json.loads(siblings.read());
  print("Num siblings: " + str(len(siblings.keys())));
  splitter = re.compile("(caliber|phekb|kclhi|covid19-phenomics)\-");
  caliber_phenoflow_siblings = list(filter(lambda sibling:"caliber" in sibling and "phekb" in sibling, siblings.keys()));
  print("Num siblings (caliber/phekb): " + str(len(caliber_phenoflow_siblings)))
  caliber_phenoflow_in_sibling = list(set(sum([[x+y,z] for x,y,z in [splitter.split(workflow) for workflow in caliber_phenoflow_siblings]],[])))
  print("Num siblings (caliber/phekb): " + str(len(caliber_phenoflow_in_sibling)))
  caliber_in_sibling = list(filter(lambda intersect:"caliber" in intersect, caliber_phenoflow_in_sibling)); 
  print("Num in sibling intersect (caliber/phekb) (caliber) " + str(len(caliber_in_sibling))); 
  phekb_in_sibling = list(filter(lambda intersect:"phekb" in intersect, caliber_phenoflow_in_sibling)); 
  print("Num in sibling intersect (caliber/phekb) (phekb) " + str(len(phekb_in_sibling)));  
 
  intersecting = list(filter(lambda intersect:len(siblings[intersect])>0, siblings));
  print("Intersecting siblings (caliber) " + str(len(list(filter(lambda sibling: len(list(filter(lambda intersection:sibling in intersection, intersecting))), caliber_in_sibling))))); 
  print("Intersecting siblings (phekb) " + str(len(list(filter(lambda sibling: len(list(filter(lambda intersection:sibling in intersection, intersecting))), phekb_in_sibling))))); 
