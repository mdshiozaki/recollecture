import React from "react";
import './App.css';
import { MDBContainer, MDBRow, MDBCol } from "mdbreact";
import 'bootstrap/dist/css/bootstrap.min.css';

class Layout extends React.Component{

  constructor () {
    super()
    this.state={
      showMe:true
    }
  }

  operation() {
    this.setState( {
      showMe:this.state.showMe

    })
  }

  render() {
    return (
    <MDBContainer>
      
      <MDBRow>
      <MDBCol md="2" >

        {
          this.state.showMe?
          <div>
          <MDBRow md="2" className ="classes-box">
          Lecture 09/10
     
          </MDBRow>
          <MDBRow md="2" className ="classes-box">
          Lecture 14/10
      
          </MDBRow>
          <MDBRow md="2" className ="classes-box">
          Lecture 21/10
      
          </MDBRow >

        
          <MDBRow md="2" className ="classes-box">
          Final Exam Review Session
      
          </MDBRow >
          </div>
          :null
        }
        

      </MDBCol>

        <MDBCol md="6" className ="text-to-speech-box">Transcript</MDBCol>
        <MDBCol md="3">
          <MDBRow md="2" className ="side-box">
            Emphasized Notes
       
          </MDBRow>
          <MDBRow md="2" className ="side-box">
            Notes
       
          </MDBRow>
          <MDBRow md="2" className ="side-box">
            Chatbot
       
          </MDBRow >
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

}

export default Layout;