import subprocess
import sys
import os

def test_prediction_e2e():
    # Run the predict script and check if it completes without error
    result = subprocess.run([sys.executable, 'src/predict.py'], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)))
    assert result.returncode == 0
    assert 'Predicted digit:' in result.stdout
