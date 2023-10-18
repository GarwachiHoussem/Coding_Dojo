var ride = [36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]
var age = [7, 8, 9, 10, 11, 12];

var mo = {
    name: 'mo',
    age: age[3],
    ride: ride[2]
}

var bo = {
    name: 'bo',
    age: age[4],
    ride: ride[5]
}

var jo = {
    name: 'jo',
    age: age[3],
    ride: ride[4]
}

function check(kids) {
    for (let i in kids) {
        console.log(kids[i].name);
        if (kids[i].age >= 10 && kids[i].ride >= 42) {
            console.log("Get on that ride kiddo");
        }
        else console.log("sorry kido maybe next year");
    }

}

check([jo, mo, bo])