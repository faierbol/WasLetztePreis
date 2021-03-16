<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">{{title}}</div>
      </v-card-title>
      <v-img :src="image_link" max-width="500" max-height="500"/>
      <v-card-text>
        <template>
          <br class="my-3">
            <div class="heading">Price: {{price}} €</div>
            <div class="heading">User: {{user.full_name}} ({{user.email}})</div>
            <div class="heading">Location: {{location}}</div>
            <div class="heading">Category: {{category}}</div>
            <br>
            <div class="subheading secondary--text">Description: {{description}}</div>
            <v-btn flat icon color="blue" @click="updateRating">
              <v-icon> {{ (this.rating === 0 ? 'thumb_up_off_alt' : 'thumb_up') }}</v-icon>
            </v-btn>
            <div class="heading">Rating: {{rating}}</div>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Back</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {dispatchGetUsers, dispatchUpdateAdvert} from '@/store/admin/actions';
import {readAdminOneAdvert, readAdminOneUser} from '@/store/admin/getters';
import {IAdvertUpdate} from '@/interfaces';

@Component
export default class DetailAdvert extends Vue {
  public valid = false;
  public title: string = '';
  public description: string = '';
  public location: string = '';
  public category: string = '';
  public price: number = 0;
  public rating: number = 0;
  public image_link: string = '';
  public owner_id: number = 0;

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.title = '';
    this.description = '';
    this.location = '';
    this.category = '';
    this.price = 0;
    this.rating = 0;
    this.image_link = '';
    this.owner_id = 0;
    this.$validator.reset();
    if (this.advert) {
      this.title = this.advert.title;
      this.description = this.advert.description;
      this.price = this.advert.price;
      this.rating = this.advert.rating;
      this.category = this.advert.category;
      this.location = this.advert.location;
      this.image_link = this.advert.image_link;
      this.owner_id = this.advert.owner_id;
    }
  }

  public cancel() {
    this.$router.back();
  }

  public async updateRating() {
    if (await this.$validator.validateAll()) {
      const updatedAdvert: IAdvertUpdate = {};
      if (this.rating === 0) {
        updatedAdvert.rating = 1;
        await dispatchUpdateAdvert(this.$store, { id: this.advert!.id, advert: updatedAdvert });
        this.rating = 1;
      } else if (this.rating === 1) {
        updatedAdvert.rating = 0;
        await dispatchUpdateAdvert(this.$store, { id: this.advert!.id, advert: updatedAdvert });
        this.rating = 0;
      }
    }
  }

  get advert() {
    return readAdminOneAdvert(this.$store)(+this.$router.currentRoute.params.id);
  }

  get user(){
    console.log(this.owner_id)
    return readAdminOneUser(this.$store)(+this.owner_id);
  }
}
</script>
