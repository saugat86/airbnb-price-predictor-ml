import { useState } from "react";
import { Card, Typography, Form, Input, Select, Button, Divider } from "antd";
import { makeModelsPost } from "../api/api";

const { Title } = Typography;
const { Option } = Select;

const formValuesInitialState = {
  host_is_superhost: "",
  host_has_profile_pic: "",
  host_identity_verified: "",
  neighbourhood_cleansed: "",
  property_type: "",
  room_type: "",
  accommodates: "",
  bathrooms_text: "",
  beds: "",
  minimum_nights: "",
  maximum_nights: "",
  maximum_minimum_nights: "",
  minimum_maximum_nights: "",
  maximum_nights_avg_ntm: "",
  minimum_nights_avg_ntm: "",
  has_availability: "",
  availability_30: "",
  availability_60: "",
  availability_90: "",
  availability_365: "",
  number_of_reviews: "",
  instant_bookable: "",
  reviews_per_month: "",
  license: "",
  latitude: "",
  longitude: "",
};

const Models = () => {
  const [formValues, setFormValues] = useState(formValuesInitialState);
  const [models, setModels] = useState(null);

  const isDisabled = !Boolean(formValues.host_is_superhost) || !Boolean(formValues.host_has_profile_pic)
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    // console.log(name, value); // Uncomment to view name/value pair
    setFormValues({ ...formValues, [name]: value });
  };



  const handleSelectChangeHostIsSuperhost = (value) => {
    setFormValues({ ...formValues, host_is_superhost: value });
  };

  const handleSelectChangeHostHasProfilePic = (value) => {
    setFormValues({ ...formValues, host_has_profile_pic: value });
  };

  const handleSelectChangeHostIdVerified = (value) => {
    setFormValues({ ...formValues, host_identity_verified: value });
  };

  const handleSelectChangeNeighbourhood = (value) => {
    setFormValues({ ...formValues, neighbourhood_cleansed: value });
  };

  const handleSelectChangePropertyType = (value) => {
    setFormValues({ ...formValues, property_type: value });
  };

  const handleSelectChangeHasAvailability = (value) => {
    setFormValues({ ...formValues, has_availability: value });
  };

  const handleSelectChangeInstantBookable = (value) => {
    setFormValues({ ...formValues, instant_bookable: value });
  };

  const handleSelectChangeRoomType = (value) => {
    setFormValues({ ...formValues, room_type: value });
  };

  const resetForm = () => {
    setFormValues(formValuesInitialState);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    //console.log(formValues);

    // Post request
    makeModelsPost(formValues).then((responseData) => {
      setModels(responseData);
    });
  };

  return (
    <Card>
      <Title>Enter Airbnb Data</Title>
      <form>
        <Form.Item label="Host is superhost">
          <Select
            name="host_is_superhost"
            defaultValue=""
            value={formValues.host_is_superhost}
            onChange={handleSelectChangeHostIsSuperhost}
          >
            <Option value="">Please choose something</Option>
            <Option value="t">Yes</Option>
            <Option value="f">No</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Host has profile pic">
          <Select
            name="host_has_profile_pic "
            defaultValue=""
            value={formValues.host_has_profile_pic}
            onChange={handleSelectChangeHostHasProfilePic}
          >
            <Option value="">Please choose something</Option>
            <Option value="t">Yes</Option>
            <Option value="f">No</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Host identity verified ">
          <Select
            name="host_identity_verified "
            defaultValue=""
            value={formValues.host_identity_verified}
            onChange={handleSelectChangeHostIdVerified}
          >
            <Option value="">Please choose something</Option>
            <Option value="t">Yes</Option>
            <Option value="f">No</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Neighbourhood">
          <Select
            name="neighbourhood_cleansed"
            defaultValue=""
            value={formValues.neighbourhood_cleansed}
            onChange={handleSelectChangeNeighbourhood}
          >
            <Option value="">Please choose something</Option>
            <Option value="ΑΜΠΕΛΟΚΗΠΟΙ">ΑΜΠΕΛΟΚΗΠΟΙ</Option>
            <Option value="ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ">
              ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ
            </Option>
            <Option value="ΚΕΡΑΜΕΙΚΟΣ">ΚΕΡΑΜΕΙΚΟΣ</Option>
            <Option value="ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ">ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ</Option>
            <Option value="ΠΑΓΚΡΑΤΙ">ΠΑΓΚΡΑΤΙ</Option>
            <Option value="ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ">
              ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ
            </Option>
            <Option value="ΣΤΑΔΙΟ">ΣΤΑΔΙΟ</Option>
            <Option value="ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ">ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ</Option>
            <Option value="ΑΚΡΟΠΟΛΗ">ΑΚΡΟΠΟΛΗ</Option>
            <Option value="ΝΕΑ ΚΥΨΕΛΗ">ΝΕΑ ΚΥΨΕΛΗ </Option>
            <Option value="ΚΟΛΩΝΑΚΙ">ΚΟΛΩΝΑΚΙ</Option>
            <Option value="ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ">
              ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ
            </Option>
            <Option value="ΠΑΤΗΣΙΑ">ΠΑΤΗΣΙΑ</Option>
            <Option value="ΓΚΑΖΙ">ΓΚΑΖΙ</Option>
            <Option value="ΑΝΩ ΠΑΤΗΣΙΑ">ΑΝΩ ΠΑΤΗΣΙΑ</Option>
            <Option value="ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ">ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ</Option>
            <Option value="ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ">ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ</Option>
            <Option value="ΙΛΙΣΙΑ">ΙΛΙΣΙΑ</Option>
            <Option value="ΘΗΣΕΙΟ">ΘΗΣΕΙΟ</Option>
            <Option value="ΠΕΔΙΟ ΑΡΕΩΣ">ΠΕΔΙΟ ΑΡΕΩΣ</Option>
            <Option value="ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ">ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ</Option>
            <Option value="ΠΕΤΡΑΛΩΝΑ">ΠΕΤΡΑΛΩΝΑ</Option>
            <Option value="ΓΟΥΒΑ">ΓΟΥΒΑ</Option>
            <Option value="1Ο ΝΕΚΡΟΤΑΦΕΙΟ">1Ο ΝΕΚΡΟΤΑΦΕΙΟ</Option>
            <Option value="ΠΡΟΜΠΟΝΑ">ΠΡΟΜΠΟΝΑ</Option>
            <Option value="ΓΟΥΔΙ">ΓΟΥΔΙ</Option>
            <Option value="ΝΕΟΣ ΚΟΣΜΟΣ">ΝΕΟΣ ΚΟΣΜΟΣ</Option>
            <Option value="ΚΟΛΩΝΟΣ">ΚΟΛΩΝΟΣ</Option>
            <Option value="ΝΙΡΒΑΝΑ">ΝΙΡΒΑΝΑ</Option>
            <Option value="ΚΥΨΕΛΗ">ΚΥΨΕΛΗ</Option>
            <Option value="ΑΝΩ ΚΥΨΕΛΗ">ΑΝΩ ΚΥΨΕΛΗ</Option>
            <Option value="ΖΑΠΠΕΙΟ">ΖΑΠΠΕΙΟ</Option>
            <Option value="ΛΥΚΑΒΗΤΤΟΣ">ΛΥΚΑΒΗΤΤΟΣ</Option>
            <Option value="ΒΟΤΑΝΙΚΟΣ">ΒΟΤΑΝΙΚΟΣ</Option>
            <Option value="ΓΚΥΖΗ">ΓΚΥΖΗ</Option>
            <Option value="ΣΕΠΟΛΙΑ">ΣΕΠΟΛΙΑ</Option>
            <Option value="ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ">ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ</Option>
            <Option value="ΠΟΛΥΓΩΝΟ">ΠΟΛΥΓΩΝΟ</Option>
            <Option value="ΠΕΝΤΑΓΩΝΟ">ΠΕΝΤΑΓΩΝΟ</Option>
            <Option value="ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ">ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ</Option>
            <Option value="ΕΛΛΗΝΟΡΩΣΩΝ">ΕΛΛΗΝΟΡΩΣΩΝ</Option>
            <Option value="ΡΗΓΙΛΛΗΣ">ΡΗΓΙΛΛΗΣ</Option>
            <Option value="ΚΟΛΟΚΥΝΘΟΥ">ΚΟΛΟΚΥΝΘΟΥ</Option>
            <Option value="ΡΙΖΟΥΠΟΛΗ">ΡΙΖΟΥΠΟΛΗ</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Property type">
          <Select
            name="property_type"
            defaultValue=""
            value={formValues.property_type}
            onChange={handleSelectChangePropertyType}
          >
            <Option value="">Please choose something</Option>
            <Option value="house">House</Option>
            <Option value="room">Room</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Room type">
          <Select
            name="room_type"
            defaultValue=""
            value={formValues.room_type}
            onChange={handleSelectChangeRoomType}
          >
            <Option value="">Please choose something</Option>
            <Option value="Entire home/apt">Entire home/apt</Option>
            <Option value="Private room">Private room</Option>
            <Option value="Hotel room">Hotel room</Option>
            <Option value="Shared room">Shared room</Option>
          </Select>
        </Form.Item>

        <Form.Item label="Accommodates">
          <Input
            type="number"
            min = "1"
            name="accommodates"
            value={formValues.accommodates}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Bathrooms">
          <Input
            type="number"
            min = "1"
            name="bathrooms_text"
            value={formValues.bathrooms_text}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Beds">
          <Input
            type="number"
            min = "1"
            name="beds"
            value={formValues.beds}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Minimum Nights">
          <Input
            type="number"
            min = "1"
            name="minimum_nights"
            value={formValues.minimum_nights}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Maximum Nights">
          <Input
            type="number"
            min = "1"
            name="maximum_nights"
            value={formValues.maximum_nights}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Maximum Min Nights">
          <Input
            type="number"
            min = "1"
            name="maximum_minimum_nights"
            value={formValues.maximum_minimum_nights}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Minimum Max Nights">
          <Input
            type="number"
            min = "1"
            name="minimum_maximum_nights"
            value={formValues.minimum_maximum_nights}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="maximum_nights_avg_ntm ">
          <Input
            type="number"
            min = "1"
            name="maximum_nights_avg_ntm"
            value={formValues.maximum_nights_avg_ntm}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="minimum_nights_avg_ntm ">
          <Input
            type="number"
            min = "1"
            name="minimum_nights_avg_ntm"
            value={formValues.minimum_nights_avg_ntm}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Has availability">
          <Select
            name="has_availability"
            defaultValue=""
            value={formValues.has_availability}
            onChange={handleSelectChangeHasAvailability}
          >
            <Option value="">Please choose something</Option>
            <Option value="t">Yes</Option>
            <Option value="f">No</Option>
          </Select>
        </Form.Item>

        <Form.Item label="availability_30">
          <Input
            type="number"
            min = "1"
            name="availability_30"
            value={formValues.availability_30}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="availability_60  ">
          <Input
            type="number"
            min = "1"
            name="availability_60"
            value={formValues.availability_60}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="availability_90  ">
          <Input
            type="number"
            min = "1"
            name="availability_90"
            value={formValues.availability_90}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="availability_365">
          <Input
            type="number"
            min = "1"
            name="availability_365"
            value={formValues.availability_365}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="number_of_reviews ">
          <Input
            type="number"
            min = "0"
            name="number_of_reviews"
            value={formValues.number_of_reviews}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Reviews per month ">
          <Input
            type="number"
            min = "0"
            name="reviews_per_month"
            value={formValues.reviews_per_month}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Instant Bookable">
          <Select
            name="instant_bookable"
            defaultValue=""
            value={formValues.instant_bookable}
            onChange={handleSelectChangeInstantBookable}
          >
            <Option value="">Please choose something</Option>
            <Option value="t">Yes</Option>
            <Option value="f">No</Option>
          </Select>
        </Form.Item>

        <Form.Item label="License">
          <Input
            name="license"
            value={formValues.license}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Latitude">
          <Input
            type="number"
            min = "1"
            name="latitude"
            value={formValues.latitude}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item label="Longitude">
          <Input
            type="number"
            min = "1"
            name="longitude"
            value={formValues.longitude}
            onChange={handleInputChange}
          />
        </Form.Item>

        <Form.Item>
          <Button type="secondary" onClick={resetForm}>
            Reset
          </Button>
          &nbsp;
          <Button type="primary" disabled ={isDisabled} onClick={handleFormSubmit}>
            Submit
          </Button>
        </Form.Item>
      </form>

      <Divider />

      {models && (
        <div>
          <Title level={3}>Price Prediction</Title>
          {JSON.stringify(models)}
        </div>
      )}
    </Card>
  );
};

export default Models;
