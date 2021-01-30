# finalproject
Factorio Final Project

Automating the Automation Game
By Ian Rackson
What is Factorio?

    Factorio is a game in which constructed entities are used to refine resources into products

How are Entities Constructed?

    Entities may be placed manually, or automatically constructed using blueprints and robots deliver materials from the player’s location to their location marked in the blueprint

Problem

    As you can see, placing blueprints takes time
    Finding the best place to stand is difficult to eyeball, especially with larger blueprints

Hypothesis

    By calculating the distances between my character and each object in a given blueprint at every location within the area of the blueprint, I can find the location from which I may deploy my robots that minimizes the time it takes to lay down all entities

More on Blueprints

    Blueprints can be recorded in json files
    In the json file for a given blueprint, each entity type is listed along with its respective x and y coordinates

Approach

    Create a python script to extract entity location information from a given blueprint json file
    Create an array of all possible locations from which I can deploy the blueprint
    For each location, calculate sum of the distances (there and back) to each entity
    Present the location that minimizes time cost

Data Sources

    Blueprints may be created in game, or found at factorioprints.com
    Blueprint strings may be decoded into jsons at https://burnysc2.github.io/Factorio/Tools/DecodeBlueprint/


How the Program Works

    The user is first asked to input the name of the json blueprint file.
    The user is then asked to indicate the accuracy with which they would like to run the program. For small blueprints, an accuracy of 1 is appropriate. For larger blueprints, a higher accuracy number will reduce computation time.
    In the actual code, increasing the accuracy works by skipping possible points to be interated over when it comes to finding totalDistance
