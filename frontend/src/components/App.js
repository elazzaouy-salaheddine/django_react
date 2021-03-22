import React, {Component,Fragment} from "react";
import {render} from "react-dom";

import Base from '../layout/Base';


class App extends Component {

  render() {
    return (
       <> 
       <Base/>
       </>
    )
  }
}

export default App;

const container = document.getElementById("app");
render( < App / > , container);
