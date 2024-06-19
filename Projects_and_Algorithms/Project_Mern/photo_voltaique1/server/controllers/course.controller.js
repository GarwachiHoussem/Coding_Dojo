const Course=require('../models/course');

// Create 
module.exports.createCourse= (req,res)=>{
    Course.create(req.body)
    .then((course)=> res.json(course))
    .catch((err)=> res.json(err))
};

// GET ALL
module.exports.getAllCourse =(req,res)=>{
    Course.find()
    .then((courses)=>res.json(courses))
    .catch((err)=> res.json(err))
};
// GET ONE BY ID

module.exports.getOneCourseById =(req,res)=>{
    Course.findById({_id: req.params.id})
    .then((course)=>res.json(course))
    .catch((err)=> res.json(err))
};

// DELETE
module.exports.deleteOneCourse =async (req, res) => {
    Course.findByIdAndDelete({ _id: req.params.id })
    .then((course)=>res.json(course))
    .catch((err)=>res.json(err))
};

// UPDATE by iD

module.exports.updateCourseById =(req,res)=>{
    Course.findByIdAndUpdate({_id:req.params.id}, req.body, {
        new: true,
        runValidators: true
    })
    .then((updateCourse)=>res.json(updateCourse))
    .catch((err)=> res.status(400).json(err));
};