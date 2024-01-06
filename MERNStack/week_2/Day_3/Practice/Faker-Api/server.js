const express = require("express");
const Company = require("./models/Company");
const app = express();
const port = 8000;

// req is shorthand for request
// res is shorthand for response
const User = require("./models/User");

app.get("/api/users/new", (request, response) => {
    response.json(new User());
});
app.get("/api/companies/new", (request, response) => {
    response.json(new Company());
});

app.get("/api/user/company", (request, response) => {
    response.json({ user: new User(), company: new Company() });
});
app.listen(port, () => console.log(`the server is up & run on PORT: ${port}`));
