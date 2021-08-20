<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">{{title}}</div>
      </v-card-title>
      <v-img :src="imageLink" max-width="500" max-height="500"/>
      <v-card-text>
        <template>
          <br class="my-3">
            <div class="heading">Price: {{price}} €</div>
            <div class="heading">User: {{ ownerName }} ({{ ownerMail }})</div>
            <div class="heading">Location: {{location}}</div>
            <div class="heading">Category: {{category}}</div>
            <br>
            <div class="subheading secondary--text">Description: {{description}}</div>
<!--            <v-btn flat icon color="blue" @click="updateRating">-->
<!--              <v-icon> {{ (this.rating === 0 ? 'thumb_up_off_alt' : 'thumb_up') }}</v-icon>-->
<!--            </v-btn>-->
<!--            <div class="heading">Rating: {{rating}}</div>-->
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn v-if="currentUser.id === this.owner_id" :to="{name: 'main-adverts-edit', params: {id: advert.id, title: advert.title, description: advert.description, price: advert.price, category: advert.category, location: advert.location, image_link: advert.image_link}}">Edit</v-btn>
        <v-btn @click="cancel">Back</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { dispatchGetUsers } from '@/store/main/actions';
import { readOneUser } from '@/store/main/getters';
import { readOneAdvert, readUserProfile } from '@/store/main/getters';

@Component
export default class DetailAdvert extends Vue {
  public valid = false;
  public title: string = '';
  public description: string = '';
  public location: string = '';
  public category: string = '';
  public price: number = 0;
  public imageLink: string = '';
  public owner_id: number = 0;
  public ownerName: string = '';
  public ownerMail: string = '';

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
    this.imageLink = '';
    this.owner_id = 0;
    this.$validator.reset();
    if (this.advert) {
      this.title = this.advert.title;
      this.description = this.advert.description;
      this.price = this.advert.price;
      this.category = this.advert.category;
      this.location = this.advert.location;
      this.imageLink = this.advert.image_link;
      this.owner_id = this.advert.owner_id;
    }
    if (this.owner) {
      this.ownerName = this.owner.full_name
      this.ownerMail = this.owner.email
    }
  }

  public cancel() {
    this.$router.back();
  }

  // public async updateRating() {
  //   if (await this.$validator.validateAll()) {
  //     const updatedAdvert: IAdvertUpdate = {};
  //     if (this.rating === 0) {
  //       updatedAdvert.rating = 1;
  //       await dispatchUpdateAdvert(this.$store, { id: this.advert!.id, advert: updatedAdvert });
  //       this.rating = 1;
  //     } else if (this.rating === 1) {
  //       updatedAdvert.rating = 0;
  //       await dispatchUpdateAdvert(this.$store, { id: this.advert!.id, advert: updatedAdvert });
  //       this.rating = 0;
  //     }
  //   }
  // }

  get advert() {
    return readOneAdvert(this.$store)(+this.$router.currentRoute.params.id);
  }

  get owner() {
    return readOneUser(this.$store)(+this.owner_id);
  }

  get currentUser() {
    return readUserProfile(this.$store);
  }
}
</script>
