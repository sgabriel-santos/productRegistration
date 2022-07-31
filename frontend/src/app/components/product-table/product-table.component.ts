import { Component, OnInit } from '@angular/core';
import { Product } from 'src/app/interfaces/product';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-product-table',
  templateUrl: './product-table.component.html',
  styleUrls: ['./product-table.component.scss']
})
export class ProductTableComponent implements OnInit {
  
  products: Product[] = [];
  realProducts: Product[] = []

  constructor(private productService: ProductService) {}

  ngOnInit(): void {
    this.getProcucts();
  }

  getProcucts(): void {
    this.productService.getProducts()
        .subscribe(products => {
          this.products = products;
          this.realProducts = products
        });
  }

  onInputChange(event: any){
    let input_value = event.target.value
    this.products = this.realProducts.filter(value => {
      return value.description.toLocaleLowerCase().includes(input_value.trim().toLocaleLowerCase())
    })
  }

  delete(product_id: any): void {
    this.productService.deleteProduct(product_id).subscribe(_ => {
      this.realProducts = this.realProducts.filter(product => product.id !== product_id);
      this.products = this.products.filter(product => product.id !== product_id);
    })
  }
}
