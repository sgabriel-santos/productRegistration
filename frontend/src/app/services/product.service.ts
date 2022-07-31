import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Product } from '../interfaces/product';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private url = 'http://127.0.0.1:8000/product';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient) { }

  /** GET Products from the server */
  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.url)
  }

  /** GET product by id. Will 404 if id not found */
  getProduct(id: number): Observable<Product> {
    const url = `${this.url}/${id}`;
    return this.http.get<Product>(url, {responseType:'json'})
  }

  /* GET Products whose name contains search term */
  searchProducts(term: string): Observable<Product[]> {
    if (!term.trim()) {
      // if not search term, return empty product array.
      return of([]);
    }
    return this.http.get<Product[]>(`${this.url}/?name=${term}`)
  }

  /** POST: add a new Product to the server */
  addProduct(product: Product): Observable<Product> {
    return this.http.post<Product>(this.url, {
        description: product.description, 
        category: product.category, 
        price: product.price, 
        date: product.date}, 
        this.httpOptions)
  }

  /** PUT: update the product on the server */
  updateProduct(product: Product, id: number): Observable<any> {
    return this.http.put(`${this.url}/${id}`, product, this.httpOptions)
  }

  /** DELETE: delete the product from the server */
  deleteProduct(id: number): Observable<any> {
    const url = `${this.url}/${id}`;
    return this.http.delete<Product>(url, this.httpOptions)
  }
}
