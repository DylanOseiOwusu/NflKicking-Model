import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
 

def load_excel_file(file_path):
    try:
        return pd.ExcelFile(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def read_sheets_to_dfs(xls):
    dfs = {}
    for sheet_name in xls.sheet_names:
        dfs[sheet_name] = xls.parse(sheet_name)
    return dfs

def main():
    # Define the file paths for the datasets
    file_paths = {
        'Data.xlsx': r'C:\Users\dylan\OneDrive\Desktop\NFL.Data\Data.xlsx',
    }

    # Load and merge data
    dfs = {}
    for file_name, file_path in file_paths.items():
        xls = load_excel_file(file_path)
        if xls is None:
            return  # Exit if loading fails
        dfs.update(read_sheets_to_dfs(xls))

    # List of sheet names you want to use
    sheet_names = ['Fg_Attempt', 'Fg_Made']  # Update these with your actual sheet names

    try:
        # Merge 'Fg_Attempt' and 'Fg_Made' DataFrames
        data = pd.merge(dfs['Fg_Attempt'], dfs['Fg_Made'], on='Team', how='outer')

        # Debugging output to understand data dimensions and alignment
        print(f"Dimensions of data after merge: {data.shape}")

        # Prepare features and target
        features = data['2LSeaAtt'].values.reshape(-1, 1)  # Reshape for single feature
        target = data['2LSeaMade'].values

        # Print out unique teams or other relevant information for debugging
        print(f"Unique teams in merged data: {data['Team'].unique()}")

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        # Debugging output to verify dimensions after splitting
        print(f"Dimensions of X_train: {X_train.shape}, y_train: {y_train.shape}")
        print(f"Dimensions of X_test: {X_test.shape}, y_test: {y_test.shape}")

        # Check for NaN values in target arrays
        if pd.isnull(y_train).any() or pd.isnull(y_test).any():
            print("Warning: NaN values found in target arrays.")

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        predictions = model.predict(X_test)

        # Evaluate the model
        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        # Print evaluation metrics
        print(f'\nEvaluation Metrics:')
        print(f'MAE: {mae}, MSE: {mse}, R2: {r2}')

       # Predict '2LSeaMade' for the 2024 season based on '2LSeaAtt'
        average_2LSeaAtt_2024 = data['2LSeaAtt'].mean()  # Calculate average value of '2LSeaAtt'
        predicted_2LSeaMade_2024 = model.predict([[average_2LSeaAtt_2024]])

        print(f"Projected '2LSeaMade' for 2024 season: {predicted_2LSeaMade_2024[0]}")

        # Visualize the data and the regression line
        plt.scatter(features, target, color='blue', label='Actual data')
        plt.plot(features, model.predict(features), color='red', label='Regression line')
        plt.scatter(average_2LSeaAtt_2024, predicted_2LSeaMade_2024, color='green', marker='o', label='Projected 2024 League Average')
        #Annotate points with team abbreviations
        for i, team in enumerate(data['Team']):
         plt.annotate(team, (features[i], target[i]), textcoords="offset points", xytext=(0, 5), ha='center')
        plt.xlabel('2LSeaAtt')
        plt.ylabel('2LSeaMade')
        plt.title('Field Goals Made vs. Field Goals Attempted')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Failed to merge DataFrames: {str(e)}")

if __name__ == "__main__":
    main()
