import React from "react"
import Nav from "./components/Nav/Nav";
import './app.css'
import Quotes from "./pages/Quotes/Quotes";

const App = ()=> {
	return (
		<div>
			<Nav/>
            <Quotes/>
		</div>
	);
}

export default App;