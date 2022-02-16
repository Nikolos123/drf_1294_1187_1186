import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import AuthorList from "./components/Author.js";
import BookList from "./components/Book.js";
import NotFound404 from "./components/NotFound404.js";
import BookListAuthors from "./components/BooksAuthor.js";
import {HashRouter, Route, BrowserRouter, Link, Switch,Redirect} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
        };
    }
    componentDidMount() {
        // const authors = [
        //     {
        //         'first_name': 'Фёдор',
        //         'last_name': 'Достоевский',
        //         'birthday_year': 1821,
        //     },
        //     {
        //         'first_name': 'Александр',
        //         'last_name': 'Грин',
        //         'birthday_year': 1880,
        //     }
        // ]
        axios.get('http://127.0.0.1:8001/api/authors/').then(response => {
            this.setState({
                'authors': response.data
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8001/api/books/').then(response => {
            this.setState({
                'books': response.data
            })
        }).catch(error => console.log(error))


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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}/>}/>

                         <Route path='/author/:id'>

                             <BookListAuthors books={this.state.books} authors={this.state.authors}/>

                         </Route>

                        <Redirect from='/authors1' to='/' />
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
