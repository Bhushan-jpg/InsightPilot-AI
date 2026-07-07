import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import DatasetOverview from "./pages/DatasetOverview";


function App(){

return (

<BrowserRouter>

    <Routes>


        <Route
        path="/"
        element={<Login />}
        />


        <Route
        path="/dashboard"
        element={<Dashboard />}
        />


        <Route
        path="/dataset"
        element={<DatasetOverview />}
        />


    </Routes>

</BrowserRouter>

)

}


export default App;