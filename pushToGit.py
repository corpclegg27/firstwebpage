import subprocess
import sys
import datetime

def run_git_command(command):
    """Executes a terminal command and handles errors."""
    try:
        # shell=True allows us to run commands exactly as we would in the terminal
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {command}")
        print(e.stderr.strip())
        sys.exit(1)

def main():
    print("🚀 Starting auto-sync to GitHub...\n")

    # 1. Determine the commit message
    # If you pass a message when running the script, it uses that.
    # Otherwise, it auto-generates a timestamped message.
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')
        commit_message = f"Auto-sync update: {current_time}"

    # 2. Stage all changes
    print("📦 Staging files (git add .)...")
    run_git_command("git add .")

    # 3. Commit the changes
    print(f"📝 Committing changes: '{commit_message}'...")
    run_git_command(f'git commit -m "{commit_message}"')

    # 4. Push to the remote repository
    print("☁️ Pushing to remote (git push origin main)...")
    # Note: If your default branch is 'master', change 'main' to 'master' below
    run_git_command("git push origin main")

    print("\n✅ Successfully synced to GitHub! Vercel is now deploying your changes.")

if __name__ == "__main__":
    main()