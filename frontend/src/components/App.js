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





{/*   constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("/client-api/clients/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
        {this.state.data.map(Opc => {
          return (
            <li key={Opc.id}>
              {Opc.raison_social}
            </li>
          );
        })}

      </ul>
    );
  }
 */}