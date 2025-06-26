import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_qsr_sales_data():
    """Generate synthetic QSR sales data for 50 stores over 2 years"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    print("Generating QSR sales data...")
    
    # Date range: 2 years of daily data
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Store configurations
    stores = [f"STORE_{str(i).zfill(3)}" for i in range(1, 51)]
    store_types = ['Urban', 'Suburban', 'Highway', 'Mall', 'Airport']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Create store metadata
    store_metadata = []
    for store_id in stores:
        metadata = {
            'store_id': store_id,
            'store_type': random.choice(store_types),
            'region': random.choice(regions),
            'avg_daily_baseline': random.randint(800, 2500),
            'size_factor': random.uniform(0.8, 1.3)
        }
        store_metadata.append(metadata)
    
    store_df = pd.DataFrame(store_metadata)
    
    # Generate daily sales data
    all_data = []
    
    # Day of week multipliers (Monday=0 to Sunday=6)
    dow_multipliers = [0.8, 0.85, 0.9, 0.95, 1.2, 1.3, 1.1]
    
    # Seasonal multipliers by month
    seasonal_multipliers = [0.85, 0.9, 1.0, 1.05, 1.1, 1.15, 1.2, 1.15, 1.0, 0.95, 1.1, 1.25]
    
    # Store type multipliers
    type_multipliers = {'Urban': 1.1, 'Suburban': 1.0, 'Highway': 0.9, 'Mall': 1.2, 'Airport': 1.3}
    
    # Holiday dates (major ones that affect QSR)
    holidays = [
        '2022-01-01', '2022-07-04', '2022-11-24', '2022-12-25',
        '2023-01-01', '2023-07-04', '2023-11-23', '2023-12-25'
    ]
    
    print(f"Generating data for {len(stores)} stores across {len(date_range)} days...")
    
    for _, store in store_df.iterrows():
        for date in date_range:
            # Base factors
            baseline = store['avg_daily_baseline']
            
            # Day of week effect
            dow = date.weekday()
            dow_effect = dow_multipliers[dow]
            
            # Seasonal effect
            month = date.month
            seasonal_effect = seasonal_multipliers[month - 1]
            
            # Holiday effect
            holiday_effect = 0.4 if date.strftime('%Y-%m-%d') in holidays else 1.0
            
            # Weather effect (random variation)
            weather_effect = np.random.normal(1.0, 0.1)
            weather_effect = max(0.5, weather_effect)  # Ensure reasonable bounds
            
            # Store type effect
            type_effect = type_multipliers[store['store_type']]
            
            # Size factor
            size_effect = store['size_factor']
            
            # Calculate total sales
            total_sales = baseline * dow_effect * seasonal_effect * holiday_effect * weather_effect * type_effect * size_effect
            
            # Add some noise
            total_sales += np.random.normal(0, 50)
            total_sales = max(0, total_sales)  # Ensure positive
            
            # Promotional effects (15% chance)
            promo_active = random.random() < 0.15
            if promo_active:
                total_sales *= 1.25
            
            # Calculate guest count
            # Average ticket varies by store type and promotions
            base_ticket = 12.5
            if store['store_type'] == 'Airport':
                base_ticket = 15.0
            elif store['store_type'] == 'Mall':
                base_ticket = 11.0
            
            avg_ticket = np.random.normal(base_ticket, 2.0)
            avg_ticket = max(5.0, avg_ticket)  # Minimum ticket
            
            guest_count = int(total_sales / avg_ticket)
            if promo_active:
                guest_count = int(guest_count * 1.4)  # More guests during promos
            
            # Recalculate actual avg ticket
            actual_avg_ticket = total_sales / guest_count if guest_count > 0 else 0
            
            # Create record
            record = {
                'date': date,
                'store_id': store['store_id'],
                'store_type': store['store_type'],
                'region': store['region'],
                'day_of_week': dow,
                'month': month,
                'quarter': (month - 1) // 3 + 1,
                'year': date.year,
                'week_of_year': date.isocalendar()[1],
                'is_weekend': dow >= 5,
                'is_holiday': holiday_effect < 1.0,
                'promotion_active': promo_active,
                'total_sales': round(total_sales, 2),
                'guest_count': guest_count,
                'avg_ticket': round(actual_avg_ticket, 2),
                'weather_factor': round(weather_effect, 3)
            }
            all_data.append(record)
    
    # Create final DataFrame
    sales_df = pd.DataFrame(all_data)
    
    # Sort by date and store
    sales_df = sales_df.sort_values(['date', 'store_id']).reset_index(drop=True)
    
    return sales_df, store_df

def main():
    """Main function to generate and save data"""
    try:
        # Generate data
        sales_data, store_data = generate_qsr_sales_data()
        
        # Save files
        sales_data.to_csv('qsr_daily_sales.csv', index=False)
        store_data.to_csv('store_metadata.csv', index=False)
        
        # Print summary statistics
        print(f"\n✅ Successfully generated data!")
        print(f"📊 Records: {len(sales_data):,} daily records")
        print(f"🏪 Stores: {len(store_data)} stores")
        print(f"📅 Date range: {sales_data['date'].min().strftime('%Y-%m-%d')} to {sales_data['date'].max().strftime('%Y-%m-%d')}")
        print(f"💰 Average daily sales: ${sales_data['total_sales'].mean():.2f}")
        print(f"👥 Average daily guests: {sales_data['guest_count'].mean():.0f}")
        print(f"🎟️ Average ticket: ${sales_data['avg_ticket'].mean():.2f}")
        
        print(f"\n📁 Files saved:")
        print(f"   - qsr_daily_sales.csv ({len(sales_data):,} rows)")
        print(f"   - store_metadata.csv ({len(store_data)} rows)")
        
        print(f"\n📋 Sample data preview:")
        print(sales_data.head(3).to_string())
        
        # Quick data validation
        print(f"\n🔍 Data validation:")
        print(f"   - Sales range: ${sales_data['total_sales'].min():.2f} - ${sales_data['total_sales'].max():.2f}")
        print(f"   - Guest count range: {sales_data['guest_count'].min()} - {sales_data['guest_count'].max()}")
        print(f"   - Missing values: {sales_data.isnull().sum().sum()}")
        
    except Exception as e:
        print(f"❌ Error generating data: {e}")

if __name__ == "__main__":
    main()
