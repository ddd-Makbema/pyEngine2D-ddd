import json
from pyEngine2D_ddd.game_object import GameObject
from pyEngine2D_ddd.exceptions import NoInstanceError
from pyEngine2D_ddd import game_loop

class DataLoad():

    def __init__(self, game_loop_inst):
        self.game_loop_inst = game_loop_inst

    def save_game_objects(self):
        final_save_data = []
        for game_object in GameObject.INSTANCES:
            if game_object.name == "collision handler" or game_object.name == "origin":
                continue
            temp_save_go = {}
            temp_save_go["name"] = game_object.name
            temp_save_go["sprite"] = game_object.sprite
            temp_save_go["parent"] = game_object.parent
            for script in game_object.package_instances:
                    temp_save_go[script.__class__.__name__] = script.save_attributes()    
            final_save_data.append(temp_save_go)
        with open("pyEngine2D_ddd/data/game_objects.json", "w") as f:   
            f.write(json.dumps(final_save_data, indent=4))   

    def import_game_object_data(self):
        with open("pyEngine2D_ddd/data/game_objects.json", "r") as f:
            load = json.load((f))
        return load

    def instantiate_game_object(self, info, screen):
        for go in info:
            scripts = ""
            script_attributes = []
            for i in go.keys():
                if i != "name" and i != "screen" and i != "sprite" and i != "parent": 
                    scripts = scripts + ',' + "'" + go[i]['name'] + "'" # format ,file.class,file2.class2 etc.
                    script_attributes.append([i, go[i]])

            command = f"GameObject(go['name'], screen, go['sprite'], go['parent'] {scripts})"
            exec(command)
            for attr in script_attributes:
                for attr_in_script in attr[1].keys():
                    if attr_in_script != "name":
                        exec(f"GameObject.GAME_OBJECTS[go['name']].{attr[0]}.{attr_in_script} = {attr[1][attr_in_script]}")

    def remove_game_object(self, name):
        all_game_objects = self.import_game_object_data()
        for game_object in all_game_objects:
            if game_object['name'] == name:
                GameObject.GAME_OBJECTS[game_object['name']].delete()
                self.save_game_objects()
                self.game_loop_inst.game_objects_changed(True)
                return
        raise NoInstanceError(name)

    def add_game_objects(self, game_object):
        current_data = self.import_game_object_data()
        temp_save_go = {}
        temp_save_go["name"] = game_object.name
        temp_save_go["sprite"] = game_object.sprite
        temp_save_go["parent"] = game_object.parent
        for script in game_object.package_instances:
            temp_save_go[script.__class__.__name__] = script.save_attributes()    
        current_data.append(temp_save_go)
        with open("pyEngine2D_ddd/data/game_objects.json", "w") as f:   
            f.write(json.dumps(current_data, indent=4))           


        #list of dicts with name an attr

"""
How this should look:

List of dicts of game objects

(all strings)
{
name
sprite name
parent
list of dicts of scripts:
    name
    attrs - keyed to attr name and value

}


"""