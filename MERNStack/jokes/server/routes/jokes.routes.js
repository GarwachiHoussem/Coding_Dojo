const JokeController = require ("../controllers/jokes.controllers")

module.exports = (app) => {
    app.get("/api/jokes",JokeController.getAllJokes);
    app.post("/api/jokes",JokeController.createNewJoke);
};


// w9eft fi 21min