def analyze(response):
    return "Potential vulnerability" if "INJECTED" in response else "Safe"
