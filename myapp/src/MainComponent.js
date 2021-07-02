import React from 'react';
import styles from './App.css';
import {AgGridColumn, AgGridReact} from 'ag-grid-react';

import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';


const axios = require('axios');

class MainComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: "",
      output: "",
      rowData: [],
      columns: []
    };
  }

  handleChange = (event) => {
    this.setState({ input: event.target.value})
  }

  handleClick = (event) => {
    const {input} = this.state;
    axios.post('https://jsonplaceholder.typicode.com/todos/1', {
        "input_text": input
    })
    .then((response) => {
        console.log(response);
        this.setState({output: "Result here"});
    })
    .catch(function (error) {
        console.log(error);
    })

    event.preventDefault();
  }

  render() {
    let {rowData, columns} = this.state;
    return (
      <div>
        <form>
            <label>Enter your question</label>
            <input placeholder="Enter a text" type="text" onChange={this.handleChange} 
                value={this.state.input}/>
            <label>SQL Query</label>
            <textarea disabled={true} type="text" rows="4" value={this.state.output}/>
            <label>Table Result</label>
            <div className="ag-theme-alpine" style={{height: 200, marginTop: 10}}>
              <AgGridReact
                rowData={rowData}>
                {columns.map((column) => {
                  return (<AgGridColumn field={column.name}></AgGridColumn>);
                })}
              </AgGridReact>
            </div>
            <button onClick={this.handleClick}>Submit</button> 
        </form>
      </div>
    );
  }
}

export default MainComponent;
