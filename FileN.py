Run the command :
npm init

The create file index.js .

Run the command in cmd: 
npm i express –save 

Write the following code in index.js :
const express=require("express");
const app=express();

Create a new folder :public
 
Inside public create file index.html

Add some html code inside index.html :
Add the following code in index.js :
app.use(express.static('public'))
app.listen(3000,()=>{
    console.log("Application is started");
})

Run the command :
node index.js
