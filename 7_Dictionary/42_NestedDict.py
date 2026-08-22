# nested dictionaries in python are dictionaries that contain other dictionaries as values.

programmingLanguages = {
    "Python": {"Type": "Interpreted", "Year": 1991, "Creator" : "Guido van Rossum", "Uses": ["Web Development","Data Science", "etc"] }, 
    "Java": {"Type": "Compiled", "Year": 1995, "Creator" : "James Gosling", "Uses": ["Web Development","Mobile Development", "etc"] }, 
    "C++": {"Type": "Compiled", "Year": 1983, "Creator" : "Bjarne Stroustrup", "Uses": ["System Programming","Game Development", "etc"] },
    "JS": {"Type": "Interpreted", "Year": 1995, "Creator" : "Brendan Eich", "Uses": ["Web Development","Mobile Development", "etc"] }
}

#other way to write:
#programmingLanguages = {
    # "Python": {
    #     "Type": "Interpreted", 
    #     "Year": 1991, 
    #     "Creator" : "Guido van Rossum", 
    #     "Uses": ["Web Development","Data Science", "etc"] }, 
    # "Java": {
    #     "Type": "Compiled", 
    #     "Year": 1995, 
    #     "Creator" : "James Gosling", 
    #     "Uses": ["Web Development","Mobile Development", "etc"] }, 
    # "C++": {
    #     "Type": "Compiled", 
    #     "Year": 1983, 
    #     "Creator" : "Bjarne Stroustrup", 
    #     "Uses": ["System Programming","Game Development", "etc"] },
    # "JS": {
    #     "Type": "Interpreted", 
    #     "Year": 1995, 
    #     "Creator" : "Brendan Eich", 
    #     "Uses": ["Web Development","Mobile Development", "etc"] }

print(programmingLanguages)