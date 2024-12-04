# Spicescape 🍲  
Discover the hidden flavors of your city with **Spicescape**, a one-of-a-kind app that unearths street food stalls not found on conventional maps. Whether you're a foodie or an adventurer, Spicescape is your trusted companion for finding, exploring, and enjoying hidden culinary gems.

---

## Key Features 🚀

1. **Hidden Gem Locator**  
   Pinpoints unlisted street food stalls and vendors around you.  

2. **Crowdsourced Recommendations**  
   Access reviews and ratings submitted by food lovers just like you.  

3. **Personalized Suggestions**  
   Get tailored recommendations based on your location, preferences, and history.  

4. **Interactive Map**  
   Explore food stalls through a sleek and intuitive map interface.  

5. **Real-Time Updates**  
   Stay informed about operational timings, menu changes, and live events.  


---

## How Spicescape Works ⚙️  
Spicescape uses advanced algorithms to deliver accurate, real-time recommendations and mapping services:  






---

## Core Algorithms and Formulas ⚙️

### 1. Haversine Formula 🌍  
The Haversine formula calculates the great-circle distance between two points on a sphere, enabling accurate proximity filtering for food stalls.

**Formula:**  
```markdown
$$
d = 2r \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\phi_2 - \phi_1}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\lambda_2 - \lambda_1}{2}\right)}\right)
$$
```

- \( d \): Distance between two points (in kilometers or miles)  
- \( r \): Radius of the Earth (approx. **6371 km**)  
- \( \phi_1, \phi_2 \): Latitudes of the two points (in radians)  
- \( \lambda_1, \lambda_2 \): Longitudes of the two points (in radians)  

**Use Case in Spicescape:**  
This formula helps in filtering nearby food stalls based on user location.

---

### 2. Bounding Box Filtering 📦  
Bounding box filtering is used to create a rectangular geographic area for quick search results by minimizing the Haversine calculations.

**Formulas:**  
For the **minimum and maximum latitude**:  
```markdown
$$
\text{min\_lat} = \phi - \frac{\text{radius}}{r}
$$
$$
\text{max\_lat} = \phi + \frac{\text{radius}}{r}
$$
```

For the **minimum and maximum longitude**:  
```markdown
$$
\text{min\_lon} = \lambda - \arcsin\left(\frac{\text{radius}}{r \cdot \cos(\phi)}\right)
$$
$$
\text{max\_lon} = \lambda + \arcsin\left(\frac{\text{radius}}{r \cdot \cos(\phi)}\right)
$$
```

- \( \phi, \lambda \): Latitude and longitude of the center point (in radians)  
- \( \text{radius} \): Search radius (in kilometers or miles)  
- \( r \): Radius of the Earth (approx. **6371 km**)  

**Use Case in Spicescape:**  
Bounding box filtering narrows down the search area before applying precise calculations like Haversine.

---

### 3. Tokenization (Text Preprocessing for Search) ✂️  
Tokenization breaks text input (e.g., food stall names or reviews) into smaller components for better search and NLP processing.

**Tokenization Process:**  
1. Convert text to lowercase:  
   ```python
   input_text.lower()
   ```
2. Remove punctuation:  
   ```python
   re.sub(r'[^\w\s]', '', input_text)
   ```
3. Split text into tokens:  
   ```python
   tokens = input_text.split()
   ```

**Example:**  
For input `“Best hot dogs in town!”`:
- **Step 1:** Convert to lowercase: `"best hot dogs in town"`  
- **Step 2:** Remove punctuation: `"best hot dogs in town"`  
- **Step 3:** Split into tokens: `["best", "hot", "dogs", "in", "town"]`  

**Use Case in Spicescape:**  
Tokenization is used in search functionalities, enabling fast and accurate food stall lookups based on keywords or reviews.

---

## Example Integrations 🔗  

- **Haversine Distance:** Quickly find nearby food stalls using precise distance calculations.  
- **Bounding Box Filtering:** Narrow down search areas to improve performance for large datasets.  
- **Tokenization:** Enhance search accuracy for queries like `"best biryani near me."`

---

## **Crowdsourced Data Aggregation**  
Users contribute directly to Spicescape by submitting stall details, reviews, and photos. These are processed using a blend of **natural language processing (NLP)** and **sentiment analysis** to provide meaningful recommendations.

---

## Getting Started 🛠️

### Backend Setup
Follow these steps to get the Spicescape backend running locally:

#### 1️⃣ Clone the Repository
Clone the project to your local system and navigate to the `/backend` directory:
```bash
git clone <repository_url>
cd spicescape/backend
```

#### 2️⃣ Create a `.env` File
Inside the `/backend` folder, create a file named `.env` and add the following variables:
```env
POSTGRES_DB=spicescape_db
POSTGRES_USER=spicescape_user
POSTGRES_PASSWORD=spicescape_password
SECRET_KEY=mysecretkey123
```

#### 3️⃣ Build and Start the Backend
Run the following command:
```bash
docker-compose up --build
```

#### 4️⃣ Access the Backend
Once the backend is running, you can access it at:
```
http://localhost:8000/api/food-stalls/
```

Example Query Parameters:  
- Filter by cuisine:  
  ```
  http://localhost:8000/api/food-stalls/?cuisine=italian
  ```
- Filter by location and radius:  
  ```
  http://localhost:8000/api/food-stalls/?latitude=17.3850&longitude=78.4867&radius=2
  ```

#### Backend Commands:
- **Populate food stall data**:  
  ```bash
  python manage.py populate_food_stalls data.csv
  ```
- **Retrieve nearby stalls**:  
  ```bash
  python manage.py retrieve_nearby_stalls 17.3850 78.4867 5
  ```

---

### Frontend Setup
The frontend is designed with React for a smooth, user-friendly experience. Here’s how to set it up:

#### 1️⃣ Install Dependencies
Navigate to the `/frontend` folder and run:
```bash
npm install
```

#### 2️⃣ Start the Application
Use the following command to build and run the frontend:
```bash
docker-compose up --build
```
Visit `http://localhost:3000` in your browser.

---

## Future Enhancements 🌟
1. **AI-Driven Recommendations**  
   Implement advanced machine learning models for even more accurate suggestions.  

2. **Enhanced UI/UX**  
   Introduce modern design patterns and animations for a richer user experience.  

3. **Gamification Features**  
   Add badges, achievements, and leaderboards to incentivize exploration.  

4. **Vendor Integration**  
   Allow vendors to directly update their profiles and share promotions with users.  

---

## Contributing 🤝
We welcome contributions from the community! If you’d like to help improve Spicescape, feel free to fork the repository, make your changes, and submit a pull request.

---

## License 📄
Spicescape is licensed under the MIT License. See the `LICENSE` file for details.

--- 
