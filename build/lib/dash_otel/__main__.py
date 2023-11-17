from dash_otel.app import app

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8000)

# from pkg_resources import iter_entry_points
# from opentelemetry.instrumentation.dependencies import get_dist_dependency_conflicts
# value = list(iter_entry_points("opentelemetry_instrumentor"))
# get_dist_dependency_conflicts(value[0].dist)