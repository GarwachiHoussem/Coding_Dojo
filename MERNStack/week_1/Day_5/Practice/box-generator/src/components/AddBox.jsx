import React from 'react'

const AddBox = (props) => {
    const { boxes, setBoxes } = props
    const AddHandler = (e)=> {
        e.preventDefault()
        console.log(e.target[0].value);
        setBoxes([...boxes,e.target[0].value])
        console.log(boxes);
    
    }
    return (
        <div><h1>Box Generator</h1>
            <form onSubmit={(e)=>AddHandler(e)}>
                <label >
                    color
                    <input />
                    <button type="submit">Add</button>
                </label>
            </form>

        </div>
    )
}

export default AddBox
