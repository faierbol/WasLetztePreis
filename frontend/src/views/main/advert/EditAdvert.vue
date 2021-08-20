<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Advert</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form
            v-model="valid"
            ref="form"
            lazy-validation>
            <v-text-field
              label="Title"
              v-model="title"
            ></v-text-field>
            <v-text-field
              label="Description"
              v-model="description"
            ></v-text-field>
            <v-text-field
              label="Price"
              v-model="price"
            ></v-text-field>
            <v-text-field
              label="Category"
              v-model="category"
            ></v-text-field>
            <v-text-field
              label="Location"
              v-model="location"
            ></v-text-field>
            <v-text-field
              label="Image Link"
              v-model="imageLink"
            ></v-text-field>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn
          @click="submit"
          :disabled="!valid">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { dispatchGetUsers } from '@/store/main/actions';
import { dispatchUpdateAdvert } from "@/store/main/actions";
import { IAdvertUpdate } from '@/interfaces';
import { readOneUser } from "@/store/main/getters";

@Component
export default class EditAdvert extends Vue {
  public valid = false;
  public title: string = '';
  public description: string = '';
  public price: number = 0;
  public category: string = '';
  public location: string = '';
  public imageLink: string = '';

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.title = this.$route.params.title
    this.description = this.$route.params.description
    this.price = parseInt(this.$route.params.price)
    this.category = this.$route.params.category
    this.location = this.$route.params.location
    this.imageLink = this.$route.params.image_link
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedAdvert: IAdvertUpdate = {};
      if (this.title) {
        updatedAdvert.title = this.title;
      }
      if (this.description) {
        updatedAdvert.description = this.description;
      }
      if (this.price) {
        updatedAdvert.price = this.price;
      }
      if (this.category) {
        updatedAdvert.category = this.category;
      }
      if (this.location) {
        updatedAdvert.location = this.location;
      }
      if (this.imageLink) {
        updatedAdvert.image_link = this.imageLink;
      }
      await dispatchUpdateAdvert(this.$store, { id: parseInt(this.$route.params.id), advert: updatedAdvert });
      this.$router.push('/main/adverts');
    }
  }

  get user() {
    return readOneUser(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
