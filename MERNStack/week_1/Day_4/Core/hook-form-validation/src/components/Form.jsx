import React, { useState } from 'react'
// Class ---> App.jsx---><>
    //   <Form />
    //   </>
const Form = () => {

    const [ firstname, setFirstname ] = useState('')
    const [ lastname, Setlastname ] = useState('')
    const [ email, Setemail ] = useState('')
    const [ password, Setpassword ] = useState('')
    const [ confirmpassword, Setconfirmpassword ] = useState('')

    const createUser = (e) => {
        // we must prevent the default refresh of the browser to keep our state from being reset
        e.preventDefault();
    };

    return (
        <fieldset>
        <form  onSubmit={ createUser }>
            <fieldset>
        <div>
                <label>Firstname :</label> 
                <input type="text" onChange={ (e) => setFirstname(e.target.value) } />
                {firstname.length <2 ? <p style={{color:"blue"}}> First Name must be at least 2 characters</p> : <p>First Name valid</p>} 
            </div>
            </fieldset>

           <fieldset>
            <div>
                <label>Lastname : </label> 
                <input type="text" value={lastname} onChange={ (e) => Setlastname(e.target.value) } />
                {lastname.length <2 ? <p style={{color:"blue"}}> Last Name must be at least 2 characters</p> : <p>Last Name valid</p>}
            </div>
            </fieldset>
            <fieldset>
            <div>
                <label> Email : </label> 
                <input type="email" value={email} onChange={ (e) => Setemail(e.target.value) } />
                {email.length <5 ? <p style={{color:"blue"}}> Email must be at least 5 characters</p> : <p>Email valid</p>}
            </div>
            </fieldset>
            <fieldset>
            <div>
                <label> Password :</label> 
                <input type="password" value={password} onChange={ (e) => Setpassword(e.target.value) } />
                {password.length <8 ? <p style={{color:"blue"}}> Password must be at least 2 characters</p> : <p>Password valid</p>}
            </div></fieldset>
            <fieldset>
            <div>
                <label> Confirmpassword : </label> 
                <input type="password" value={confirmpassword} onChange={ (e) => Setconfirmpassword(e.target.value) } />
                {confirmpassword!= password ? <p style={{color:"blue"}}s>password must match </p> : <p></p>}
            </div></fieldset>
        </form>
        
        </fieldset>
    )
}

export default Form