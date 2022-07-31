import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.scss']
})
export class ProductDetailComponent implements OnInit {
  @Input() product: any = {};
  category = ['Livro', 'Acessórios', 'Eletrônico']

  constructor(private route: ActivatedRoute,
    private productService: ProductService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.productService.getProduct(id)
    .subscribe(product =>  this.product = product);
  }

  onChangeProduct(){
    console.log(this.product)
    this.productService.updateProduct(this.product, this.product.id).subscribe(_ =>
      this.router.navigate(['/'])
    )
  }
}
