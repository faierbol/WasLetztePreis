<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Advert</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Title" v-model="title" required></v-text-field>
            <v-text-field label="Description" v-model="description"></v-text-field>
            <v-text-field label="Price" v-model="price" hint="Please use periods: '6.5'" required></v-text-field>
            <v-text-field label="Category" v-model="category" required></v-text-field>
            <v-text-field label="Location" v-model="location" required></v-text-field>
            <v-text-field label="Image Link" v-model="imageLink" required></v-text-field>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid">
              Save
            </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {
  IAdvert,
  IAdvertUpdate,
  IAdvertCreate,
} from '@/interfaces';
import { dispatchCreateAdvert, dispatchGetAdverts } from '@/store/main/actions';
import {FB_ANALYTICS, FB_PERFORMANCE} from "@/firebase";

@Component
export default class CreateAdvert extends Vue {
  public valid = false;
  public title: string = '';
  public description: string = '';
  public price: number = 0;
  public category: string = '';
  public location: string = '';
  public imageLink: string = '';

  public async mounted() {
    FB_ANALYTICS.logEvent('Advert creation opened');
    await dispatchGetAdverts(this.$store);
    this.reset();
  }

  public reset() {
    this.title = '';
    this.description = '';
    this.price = 0;
    this.category = '';
    this.location = '';
    this.imageLink = '';
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const trace = FB_PERFORMANCE.trace('AdvertCreation');
      trace.start();
      const updatedAdvert: IAdvertCreate = {
        title: this.title,
        price: this.price,
        category: this.category,
        location: this.location,
        image_link: this.imageLink,
        inactive: false,
        rating: 0
      };
      if (this.description) {
        updatedAdvert.description = this.description;
      }

      await dispatchCreateAdvert(this.$store, updatedAdvert);
      trace.stop();
      FB_ANALYTICS.logEvent('Advert created');
      this.$router.push('/main/adverts');
    }
  }
}
</script>
