import React,{useState} from "react";
function Counter(){
    const [count,setCount]=useState(0);

    const increment=()=>{
        setCount(count+1);
    };

    return(
        <div style={{textAlign:"center",marginTop:"50px"}}>

        <h2>counter application(functional component)</h2>
        <p>current count:{count}</p>
        <button onClick={increment}>counter increment</button>
        </div>

    );
}
export default Counter;
