#api to save entries in countryDictionary.json format
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pycountry as pyc 
import json
from myconstants1 import path_logs, path_resources, path_modules, Value
from logConfig1 import setup_logger

logger = setup_logger("countryDictionary", path_logs+'/countryDictionary.log')

app = Flask(__name__)
api = Api(app)


class HandleRequest6(Resource):
    global country_code
    global doc_type
    global isStatewise
    @app.route('/' , methods = ["POST"])
    
    
    def post(self):
        print("inside post method")
        data = request.get_json()
        print("data: ", data)
        json1 = ({"status" :"failed", "message" : "All fields are mandatory"})

        try:
            country_code = data["country_code"]
            print("country_code: ", country_code)
            doc_type  = data['documents'][0]['doc_type']
            print("doc_type: ", doc_type)
            isStatewise = data["documents"][0]["isStatewise"]
            print("isStatewise: ", isStatewise)
        except AttributeError:
            print("All fields are mandatory")
            logger.debug(json1)
            return json1
        print("here ")
        
        print("country_code: ", country_code)
        print("doc_type: ", doc_type)
        print("isStatewise: ", isStatewise)

        listValues = [country_code, doc_type, isStatewise]
        print("listValues: ", listValues)
        list_to_dict = dict(listValues)
        print("list_to_dict: ", list_to_dict)
        
        return list_to_dict

    
        
    #country_name = pyc.countries.country(country).name
    #print("country_name:", country_name)

    #def createDict(country, country_list, json_path):
    #    print("country_list4:", country_list)
    #    print("inside createDict")
    #    countryDictionary1 = {
    #        "country" : f"{country}" , 
    #        "documents":[
 #           {
        #        "doc_type":doc_type, 
       #         "isStatewise":isStatewise
      #          }
      #      ]
      #  },    

      #  countryDictionary = list(countryDictionary1)
      #  country_list.extend(countryDictionary)
    
     #   with open(json_path, "w") as f:
     #       print("written in json file")
     #       return json.dump(country_list,f,indent=4)     
        
    
    def extendDocument( country, country_list):
        print("country_Obj", country)

        new_doc = {
        "doc_type": f"{doc_type}",
        "isStatewise": f"{isStatewise}"
        }
      
        for obj in country_list:

            if obj["country"] == country:
                print("replace obj with new")
                obj["documents"].append(new_doc.copy())
                print("obj :", obj) 
            
                break
        else:
                print("outside if condition")
        
    
        with open(json_path, "w") as f:
            return json.dump(country_list,f,indent=4)
    
    
    def read(json_path):
        with open(json_path, "r") as file:
            country_list = json.load(file)
            print("country_list1 ", country_list)
            return country_list
        
    #country = "india" 
   # doc_type = "passport"
   # path_modules = r"E:\demo3\modules"
   # json_path = f"{path_modules}\countryDictionary.json"     
   # json_path = json_path

    def checkValueInJson(data, doc_type ,country , json_path):
        json_file = read(json_path)

        for dictionary_country in json_file:
        
            if country == dictionary_country["country"]:

                print(f"{country} is in json!")
            
                documents = dictionary_country["documents"] 

                for document in documents:
                    print("document:", document)
                    if document["doc_type"] == doc_type:
                        print(f"{doc_type} found in {country}")                    
                        break        
            
                else:
                    print(f"{doc_type} does not found in {country}")  
                    json2 = extendDocument(country, json_file)
                    return json2                              
                break
        
        else:
            print(country, "is not in json!")
            json1 = createDict(json_file, json_path)
            return json1
              
        return doc_type,country, json_path
        json1 = post(self)
        return json1
   # checkValueInJson(data, doc_type,country, json_path)


api.add_resource(HandleRequest6, '/countryDictionary')            # api endpoint 
    
if __name__ == '__main__':
    app.run(debug=False)                                    
        

        
        
    
    
    
    