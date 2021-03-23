import React, {Component,Fragment} from "react";
import {render} from "react-dom";
import Test01 from '../test/Test01';
import Test02 from '../test/Test02';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";




class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (


      <>

      <Router>
        <Switch>
          <Route exact path="/"><p>This is the home page</p></Route>
          <Route path="/test01" component={Test01} />
          <Route path="/test02" component={Test02} />
        </Switch>
      </Router>
      </>

    )
  }
}

export default App;

const container = document.getElementById("app");
render( < App / > , container);
