import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import AuthorList from "./components/Author.js";
import BookList from "./components/Book.js";
import NotFound404 from "./components/NotFound404.js";
import BookListAuthors from "./components/BooksAuthor.js";
import BookForm from "./components/BookForm";
import LoginForm from "./components/Auth.js";
import Cookies from "universal-cookie";
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from "react-router-dom";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token': '',
        };
    }

    createBook(name,author){

        const headers = this.get_headers()
        const data = {name:name,authors:author}
        axios.post('http://127.0.0.1:8001/api/books/',data,{headers}).then(

            response => {

                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({books:[]})
        })

    }

    deleteBook(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8001/api/books/${id}`,{headers}).then(

            response =>{
                this.load_data()

            }
        ).catch(error => {
            console.log(error)
            this.setState({books: []})
        })
    }



    logout(){
        this.set_token('')
    }
    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8001/api/authors/', {headers}).then(response => {
            this.setState({
                'authors': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'authors': []})
        })

        axios.get('http://127.0.0.1:8001/api/books/', {headers}).then(response => {
            this.setState({
                'books': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'books': []})
        })
    }
    is_aut(){
        return !!this.state.token
    }
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token},()=>this.load_data())
        console.log(this.state.token)
        // localStorage.setItem('token',token)
        // let token_ = localStorage.getItem('token')
        //
        // document.cookie = `token=${token},username=nikolay,password=password`

    }

    get_token_from_cookies(){
        const cookies = new Cookies()
        const token =  cookies.get('token')
        this.setState({'token': token},()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8001/api-token-auth/', {
            username: username,
            password: password
        }).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => console.log(error))

    }

    get_headers(){
        console.log('test')
        let headers = {

            'Content-Type':'application/json',
            // 'Accept': 'application/json; version=v'
        }
        // console.log(this.is_aut())
        if(this.is_aut()){
            // console.log(`Token ${this.state.token}`)
            headers['Authorization'] = `Token ${this.state.token}`
        }


        return headers
    }

    componentDidMount() {
        this.get_token_from_cookies()
        // this.load_data()
    }


    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'> Authors </Link>
                            </li>
                            <li>
                                <Link to='/books'> Books </Link>
                            </li>
                            <li>{this.is_aut()?<button onClick={()=> this.logout()}>Logout</button>:
                                <Link to='/login'> Login </Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}
                                                                              deleteBook={(id)=> this.deleteBook(id)}/>}/>

                        <Route exact path='/books/create' component={() => <BookForm authors={this.state.authors}
                                                                              createBook={(name,author)=> this.createBook(name,author)}/>}/>


                        <Route path='/author/:id'>

                            <BookListAuthors books={this.state.books} authors={this.state.authors}/>

                        </Route>
                        <Route exact path='/login'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Redirect from='/authors1' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
