from flask import Flask, url_for
app = Flask (__name__)

@app.route("/")
def home():
    url1 = url_for("Alix")
    url2 = url_for("Sam")
    url3 = url_for("Harris")
    url4 = url_for("Zachary")
    url5 = url_for("Chris")
    url6 = url_for("Felix")
    url7 = url_for("Ronald")
    output = f"""
    <center>
    <h1> <b> URLs </b> </br> 
     </br>
      <a href='{url1}'>AlixBrown</a> </br>
      <a href='{url2}'>SamRoberts</a> </br>
      <a href='{url3}'>HarrisGrills</a> </br>
      <a href='{url4}'>ZacharyWix</a> </br>
      <a href='{url5}'>ChrisPollock</a> </br>
      <a href='{url6}'>FelixMcneilly</a> </br>
      <a href='{url7}'>RonaldPlumlee</a> </br>
    </center>
      
      <h1/>   """

    return output


@app.route("/AlixBrown")
def Alix():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Alixander Brown 
    </br>
    <h1> Age:</h1> 16 
    </br>
    <h1> Hobby:</h1> Boomer 
    </br>
     <h1>Occupation:</h1> Full time idiot 
     </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>
    """
    return output
    

@app.route("/SamRoberts")
def Sam():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Sam Roberts 
    </br>
    <h1>Age:</h1> 15 
    </br>
    <h1>Hobby:</h1> Python enthusiast 
    </br>
    <h1>Occupation:</h1> Ball boy at local tenis club
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output    


@app.route("/HarrisGrills")
def Harris():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Harris Grills
    </br>
    <h1>Age:</h1> 15 
    </br>
    <h1>Hobby:</h1> Fulltime map dev for Valve.co 
    </br>
    <h1>Occupation:</h1> CEO of McDonalds international
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output


@app.route("/ZacharyWix")
def Zachary():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Zachary Wix
    </br>
    <h1>Age:</h1>15 
    </br>
    <h1>Hobby:</h1>Leader of the local Egyptian club 
    </br>
    <h1>Occupation:</h1>Vice head IT teacher at BBC
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output   


@app.route("/ChrisPollock")
def Chris():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Chris Pollok
    </br>
    <h1>Age:</h1> 15 
    </br>
    <h1>Hobby:</h1> Washed up Unity developer 
    </br>
    <h1>Occupation:</h1> n/a
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output   


@app.route("/FelixMcneilly")
def Felix():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Felix Mcneilly
    </br>
    <h1>Age:</h1> 15 
    </br>
    <h1>Hobby:</h1> Leader of the local ranger association  
    </br>
    <h1>Occupation:</h1> Professional Insurgency:Sandstorm player
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output

@app.route("/MrPlumlee")
def Ronald():
    url8 = url_for("home")
    output = f"""<h1>Name:</h1> Mr Plumlee
    </br>
    <h1>Age:</h1> 50 
    </br>
    <h1>Hobby:</h1> Coding, mainly Python but a tad bit of C## here and there 
    </br>
    <h1>Occupation:</h1> Lead dev of Python
    </br>
     </br>
     <h3>
    <a href='{url8}'>Back</a> </br> </h3>"""
    return output     


@app.route("/Dev")
def Def():
    output = """
    <centre>
    test 
    </br>
    <b> test </b>
    <h1> test </h1>
    <h1> <b> test </b> </h1>
    <strong> test </strong>
    </centre> </br> </br>
    <img src="https://steamuserimages-a.akamaihd.net/ugc/755968118243520785/0148C4080E7D69BB8597CF69A441A09E720DBDD1/?imw=150&imh=150&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true" alt="Mountain">
    """
    return output    


@app.route("/Dev2")
def Dev2():
    output = """
    <center>
    </br> </br> </br> </br> </br> </br> </br> </br> </br> </br> </br> </br>  
    <img src="https://steamuserimages-a.akamaihd.net/ugc/755968118243520785/0148C4080E7D69BB8597CF69A441A09E720DBDD1/?imw=150&imh=150&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true" alt="Mountain">
    </center>
    """
    return output     


if __name__ == "__main__":
    app.run(debug=True)