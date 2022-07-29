import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductTableComponent } from './components/product-table/product-table.component';

const routes: Routes = [
  { path: '', component: ProductTableComponent},
  { path: 'detail/:id', component: ProductTableComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
