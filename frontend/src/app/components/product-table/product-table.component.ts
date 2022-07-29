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

  constructor(private productService: ProductService) {}

  ngOnInit(): void {
    this.getProcucts();
  }

  getProcucts(): void {
    this.productService.getProducts()
        .subscribe(products => {
          this.products = products;
          console.log(products)
        });
  }

  delete(product: Product): void {
    this.productService.deleteProduct(product.id).subscribe(_ => {
      this.products = this.products.filter(h => h !== product);
    })
  }
}
