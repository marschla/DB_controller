# Template: template-ros

The repositry contains various controllers usable for the Duckietown platform (designed for the DB18)


## How to use it

### 1. Lane following procedure

Start the Duckitown lane following demo:

```shell script
 dts duckiebot demo --demo_name lane_following --duckiebot_name DUCKIEBOT_NAME --package_name duckietown_demos
```

Build the image:

```shell script
 dts devel build -f -H DUCKIEBOT_NAME.local
```

Run the controller container:

```shell script
 dts devel run -H DUCKIEBOT_NAME -L CONTROLLER_NAME.local
```


