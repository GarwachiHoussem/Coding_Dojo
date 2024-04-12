const express = require("express");
// console.log(express);

const app= express();
// console.log(express);
const PORT = 8000;

app.get("/api", (req, res) => {
    res.json({ message: "Hello World" });
});



// this needs to be below the other code blocks
app.listen( PORT, () => console.log(`Listening on port: ${PORT}`) );
