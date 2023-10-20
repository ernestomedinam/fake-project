import React, { useState } from "react";

export const SignUp = (props) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    return (
        <div className="container">
            <div className="w-100 d-flex flex-column">
                <input 
                    value={username}
                    onChange={(event) => setUsername(event.target.value)}
                    type="text" 
                    placeholder="username" />
                <input 
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                    type="password" 
                    placeholder="password" />
                <button
                    onClick={(event) => actions.signUserUp(username, password)} 
                    className="btn btn-primary">
                    {"sign up"}
                </button>
            </div>
        </div>
    );
};
