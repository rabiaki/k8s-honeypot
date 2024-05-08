const express = require("express")

const app = express()

const port = 8080;

app.get("/", (req,res) => {
  res.send("This is the server's response…")
})

app.listen(port,() => {
  console.log("Listening…")
})