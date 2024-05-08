const express = require("express")

const app = express()

const port = 8080;

app.get("/", (req,res) => {
  res.send("You got bamboozled! HEHEHE!")
})

app.listen(port,() => {
  console.log("Listening…")
})