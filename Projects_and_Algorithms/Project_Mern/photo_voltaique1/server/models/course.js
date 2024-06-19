const mongoose = require ('mongoose');

const planTypeSchema = new mongoose.Schema({
    date: { type: String, required: true },
    time: { type: String, required: true }
});
const CourseSchema= new mongoose.Schema({

    title:{
        type : String,
        required:[true, 'title must be present .'],
        minlength :[3, 'title must be at least  3 .'],
        trim:true
    },
    instructor:{
        type : String,
        required:[true, "Instructor must be present."],
    },
    details:{
        type: String,
        minlength :[10, 'Details must be at least  10 .'],
    
    },
    plan:{
        type: [planTypeSchema]
    }

}
,{timestamps: true})
module.exports=mongoose.model('Course',CourseSchema);