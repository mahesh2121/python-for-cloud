import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Blackbird script for user operations.")
    
    # Add -u argument for username
    parser.add_argument("-u", "--user", required=True, help="Specify the username")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Print output (this could be replaced with actual logic)
    print(f"Processing user: {args.user}")

if __name__ == "__main__":
    main()
